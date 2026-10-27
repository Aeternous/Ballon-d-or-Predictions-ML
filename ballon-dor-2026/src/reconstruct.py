"""Rebuild every juror's 2024 and 2025 ballot for the tracked players.

France Football publishes vote totals and some individual ballots are public,
but the complete juror-by-juror sheet was not reachable from this environment.
So each ballot is rebuilt in three steps:

1. A ballot model gives every juror a utility for every nominee:
   fitted player strength + bloc affinity (home nation, media language,
   league visibility) + verified regional tilt + noise.
2. Known ballots are pinned (anchors), and each juror gets a pool of plausible
   ballots sampled from the model.
3. Simulated annealing picks one ballot per juror so that the jury matches
   every published aggregate exactly: point totals, first-place counts,
   ballots without the player, and regional first-place splits.

Output: output/ballots_<year>.csv (one row per juror).
"""

import math
import os
import random
import sys

from common import OUT, bloc_affinity, load_json, load_jurors, points_for, write_csv

SIGMA = 4.0          # juror noise in the ballot model (utility points)
FIT_ROUNDS = 60      # strength-fitting iterations
FIT_SAMPLES = 30     # ballots per juror per fitting iteration
POOL_SAMPLES = 500   # candidate ballots sampled per juror
ANNEAL_STEPS = 1_500_000
MAX_ATTEMPTS = 6


def sample_ballot(rng, names, base, anchor):
    util = {p: base[p] + rng.gauss(0.0, SIGMA) for p in names}
    order = sorted(names, key=util.__getitem__, reverse=True)
    if anchor:
        order = [p for p in order if p not in anchor.get("exclude", ())]
        fixed = list(anchor.get("top", []))
        fixed += sorted(anchor.get("then", []), key=util.__getitem__, reverse=True)
        if fixed:
            order = fixed + [p for p in order if p not in fixed]
        for a, b in anchor.get("above", []):
            ia, ib = order.index(a), order.index(b)
            if ia > ib:
                order[ia], order[ib] = order[ib], order[ia]
    return order[:10]


def build_year(year, jurors, players, hist, seed):
    rng = random.Random(seed)
    cfg = hist[str(year)]
    active = [j for j in jurors if j["seat"] not in cfg["excluded_seats"]]
    n = len(active)
    assert n == cfg["jury_size"], (year, n)

    named = list(cfg["totals"])
    others = cfg["others"]
    names = named + others
    top3 = cfg["top3"]
    tracked = cfg["tracked"]

    tilt = {}
    for t in cfg["region_tilt"]:
        tilt[(t["confed"], t["player"])] = t["value"]

    aff = {}
    for j in active:
        aff[j["seat"]] = {
            p: bloc_affinity(j, players, p, year) + tilt.get((j["confed"], p), 0.0)
            for p in names
        }

    by_country = {}
    for j in active:
        by_country.setdefault(j["country"], []).append(j["seat"])
    anchors = {}
    for a in cfg["anchors"]:
        seats = by_country[a["country"]]
        assert len(seats) == 1, f"anchor country {a['country']} must map to one seat"
        anchors[seats[0]] = a

    # Step 1: fit player strengths so expected totals match the published totals.
    target = {p: cfg["totals"][p] / n for p in named}
    others_target = cfg["others_total"] / n
    strength = {p: target[p] for p in named}
    for p in others:
        strength[p] = others_target / len(others)
    for _ in range(FIT_ROUNDS):
        got = dict.fromkeys(names, 0.0)
        for j in active:
            base = {p: strength[p] + aff[j["seat"]][p] for p in names}
            for _ in range(FIT_SAMPLES):
                for pos, p in enumerate(sample_ballot(rng, names, base, anchors.get(j["seat"])), 1):
                    got[p] += points_for(pos)
        scale = 1.0 / (n * FIT_SAMPLES)
        for p in named:
            strength[p] += 0.5 * (target[p] - got[p] * scale)
        others_got = sum(got[p] for p in others) * scale
        for p in others:
            strength[p] += 0.5 * (others_target - others_got) / len(others)

    # Step 2: candidate pools, deduplicated on what the constraints can see.
    firsts = cfg["firsts"]
    absent = cfg["absent"]
    regional = cfg["regional_firsts"]
    dims = (
        [("total", p) for p in tracked]
        + [("first", p) for p in firsts]
        + [("field_first", None)]
        + [("absent", p) for p in absent]
        + [("regional", i) for i in range(len(regional))]
    )
    targets = (
        [cfg["totals"][p] for p in tracked]
        + [firsts[p] for p in firsts]
        + [cfg["field_firsts"]]
        + [absent[p] for p in absent]
        + [r["count"] for r in regional]
    )
    weights = [1.0 if kind == "total" else 25.0 for kind, _ in dims]

    def contribution(juror, ballot):
        pos = {p: i for i, p in enumerate(ballot, 1)}
        vec = []
        for kind, key in dims:
            if kind == "total":
                vec.append(points_for(pos.get(key)))
            elif kind == "first":
                vec.append(1 if ballot[0] == key else 0)
            elif kind == "field_first":
                vec.append(1 if ballot[0] not in top3 else 0)
            elif kind == "absent":
                vec.append(1 if key not in pos else 0)
            else:
                r = regional[key]
                vec.append(1 if juror["confed"] == r["confed"] and ballot[0] == r["player"] else 0)
        return tuple(vec)

    # Implausibility of a ballot = -log P(its first place) - sum over tracked
    # players of -log P(that player's position), using this juror's own sampled
    # marginals (with +0.5 smoothing). Scoring marginals rather than exact
    # ballots keeps e.g. a Salah-first ballot cheap for Egypt and dear elsewhere.
    pools, cost = [], []
    for j in active:
        base = {p: strength[p] + aff[j["seat"]][p] for p in names}
        first_n = dict.fromkeys(names, 0)
        pos_n = {p: [0] * 11 for p in tracked}
        seen = {}
        for _ in range(POOL_SAMPLES):
            ballot = sample_ballot(rng, names, base, anchors.get(j["seat"]))
            pos = {p: i for i, p in enumerate(ballot, 1)}
            first_n[ballot[0]] += 1
            for p in tracked:
                pos_n[p][pos.get(p, 0)] += 1
            key = (contribution(j, ballot), ballot[0])
            if key not in seen:
                seen[key] = ballot

        def implausibility(ballot):
            pos = {p: i for i, p in enumerate(ballot, 1)}
            c = -math.log((first_n[ballot[0]] + 0.5) / (POOL_SAMPLES + 0.5 * len(names)))
            for p in tracked:
                c -= math.log((pos_n[p][pos.get(p, 0)] + 0.5) / (POOL_SAMPLES + 5.5))
            return c

        # Cheapest first, so the starting point is each juror's most likely ballot.
        pool = sorted(((key[0], b, implausibility(b)) for key, b in seen.items()), key=lambda x: x[2])
        pools.append(pool)
        cost.append([c for _, _, c in pool])

    # Step 3: simulated annealing over one ballot per juror. The objective is
    # (constraint miss x penalty) + implausibility. Matching the published
    # aggregates comes first; among exact matches, the most likely set of
    # ballots wins.
    def solve(rng):
        choice = [0] * n
        agg = [0.0] * len(dims)
        for i in range(n):
            for d, v in enumerate(pools[i][0][0]):
                agg[d] += v
        implaus = sum(cost[i][0] for i in range(n))

        def miss(vec):
            return sum(w * (a - t) ** 2 for w, a, t in zip(weights, vec, targets))

        movable = [i for i in range(n) if len(pools[i]) > 1]
        for penalty, t0, t1, steps in ((20.0, 300.0, 0.1, ANNEAL_STEPS), (1000.0, 30.0, 0.01, ANNEAL_STEPS)):
            cur = penalty * miss(agg) + implaus
            for step in range(steps):
                temp = t0 * (t1 / t0) ** (step / steps)
                # Move one juror, or two at once: closing the last point of a
                # total often needs one ballot to give a point and another to take it.
                movers = rng.sample(movable, 2 if rng.random() < 0.5 else 1)
                move = [(i, rng.randrange(len(pools[i]))) for i in movers]
                if all(k == choice[i] for i, k in move):
                    continue
                trial = list(agg)
                trial_implaus = implaus
                for i, k in move:
                    for d, (o, nv) in enumerate(zip(pools[i][choice[i]][0], pools[i][k][0])):
                        trial[d] += nv - o
                    trial_implaus += cost[i][k] - cost[i][choice[i]]
                new = penalty * miss(trial) + trial_implaus
                if new <= cur or rng.random() < math.exp((cur - new) / temp):
                    for i, k in move:
                        choice[i] = k
                    agg, cur, implaus = trial, new, trial_implaus

        # Repair: if annealing left a small miss, look for the cheapest one- or
        # two-ballot change whose combined effect closes it exactly.
        for _ in range(20):
            gap = tuple(round(t - a) for a, t in zip(agg, targets))
            if not any(gap):
                break
            moves = {}
            for i in movable:
                cur_vec, cur_cost = pools[i][choice[i]][0], cost[i][choice[i]]
                for k, (vec, _, c) in enumerate(pools[i]):
                    if k != choice[i]:
                        delta = tuple(a - b for a, b in zip(vec, cur_vec))
                        moves.setdefault(delta, []).append((c - cur_cost, i, k))
            best = None
            if gap in moves:
                g, i, k = min(moves[gap])
                best = (g, [(i, k)])
            for delta, options in moves.items():
                rest = moves.get(tuple(x - d for x, d in zip(gap, delta)))
                if not rest:
                    continue
                for ga, i, ka in sorted(options)[:3]:
                    for gb, j, kb in sorted(rest)[:3]:
                        if i != j and (best is None or ga + gb < best[0]):
                            best = (ga + gb, [(i, ka), (j, kb)])
            if best is None:
                break
            for i, k in best[1]:
                for d, (o, nv) in enumerate(zip(pools[i][choice[i]][0], pools[i][k][0])):
                    agg[d] += nv - o
                choice[i] = k

        # Polish: apply exchanges that leave every aggregate unchanged but make the
        # ballots more likely: one juror's change offset exactly by another's.
        while True:
            moves = {}
            for i in movable:
                cur_vec, cur_cost = pools[i][choice[i]][0], cost[i][choice[i]]
                for k, (vec, _, c) in enumerate(pools[i]):
                    if k != choice[i]:
                        delta = tuple(a - b for a, b in zip(vec, cur_vec))
                        moves.setdefault(delta, []).append((c - cur_cost, i, k))
            for options in moves.values():
                options.sort()
            best = None
            for delta, options in moves.items():
                if options[0][0] >= 0:
                    continue
                if not any(delta):
                    gain, i, k = options[0]
                    if best is None or gain < best[0]:
                        best = (gain, [(i, k)])
                    continue
                partners = moves.get(tuple(-x for x in delta))
                if not partners:
                    continue
                for gain_a, i, ka in options[:3]:
                    if gain_a >= 0:
                        break
                    for gain_b, j, kb in partners[:3]:
                        total = gain_a + gain_b
                        if i != j and total < -1e-9 and (best is None or total < best[0]):
                            best = (total, [(i, ka), (j, kb)])
            if best is None:
                break
            for i, k in best[1]:
                choice[i] = k

        agg = [0.0] * len(dims)
        for i in range(n):
            for d, v in enumerate(pools[i][choice[i]][0]):
                agg[d] += v
        residual = {f"{kind}:{key}": round(a - t) for (kind, key), a, t in zip(dims, agg, targets) if a != t}
        return choice, residual

    # Annealing is stochastic; restart from a fresh seed until every aggregate matches.
    for attempt in range(MAX_ATTEMPTS):
        choice, residual = solve(random.Random(seed * 100 + attempt))
        if not residual:
            break

    rows = []
    for i, j in enumerate(active):
        ballot = pools[i][choice[i]][1]
        pos = {p: k for k, p in enumerate(ballot, 1)}
        anchor = anchors.get(j["seat"])
        level = anchor["level"] if anchor else "reconstructed"
        row = [j["seat"], j["country"], j["juror"], level, ballot[0]]
        for p in tracked:
            row += [pos.get(p, ""), points_for(pos.get(p))]
        rows.append(row)
    for j in jurors:
        if j["seat"] in cfg["excluded_seats"]:
            rows.append([j["seat"], j["country"], j["juror"], "no ballot", ""] + ["", 0] * len(tracked))
    rows.sort(key=lambda r: r[0])

    header = ["seat", "country", "juror", "source", "first_place"]
    for p in tracked:
        header += [f"{p} pos", f"{p} pts"]
    write_csv(os.path.join(OUT, f"ballots_{year}.csv"), header, rows)
    return residual, strength


def main():
    jurors = load_jurors()
    players = load_json("players.json")
    hist = load_json("history.json")
    ok = True
    for year, seed in ((2024, 2401), (2025, 2501)):
        residual, _ = build_year(year, jurors, players, hist, seed)
        if residual:
            ok = False
            print(f"{year}: aggregates NOT fully matched: {residual}")
        else:
            print(f"{year}: every published aggregate matched exactly")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
