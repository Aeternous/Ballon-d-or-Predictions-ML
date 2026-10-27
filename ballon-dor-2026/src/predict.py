"""Backtest the three-criteria juror model on 2024-2025, then predict 2026.

Juror j's utility for candidate c:

    U = wP_j * P_c + wT_j * T_c + wF * F_c      (the three official criteria)
        + bloc affinity                         (home nation, media language, league)
        + juror history                         (2026 only: past support for c)
        + noise ~ N(0, sigma)

Ballots are ranked by utility and scored 15-12-10-8-7-5-4-3-2-1.

Backtest: each year's top 3 are modelled by name and the rest of the ballot
by a generic field sitting `gap` points below the two leaders. wP, sigma and
gap are fitted on 2024 and 2025 under the rule that Individual Performance
carries the highest weight (wP >= wT). Fair Play is a fixed 0.10 filter.

2026: every contender in data/criteria.json is modelled by name. The
shortlisted players left out of that file are a small generic remainder,
calibrated to take the share of points that places 18-30 took in 2025.

Writes output/backtest.csv, output/prediction_2026_*.csv, output/summary.json.
"""

import json
import os
import random
import statistics

from common import OUT, bloc_affinity, load_json, load_jurors, points_for, read_csv, team_success, write_csv

W_F = 0.10
FIELD_SIZE = 7          # backtest: generic players filling places 4-10
FIELD_STEP = 1.5
REMAINDER_SIZE = 5      # 2026: generic slots for shortlisted players not modelled by name
REMAINDER_SHARE = 0.04  # places 18-30 took 4.1% of all points in 2025 (276 of 6,700)
HISTORY_GAMMA = 1.0     # utility per standard deviation of past support for the same player
LEAN_BETA = 0.05        # weight shift per unit of a juror's output-over-silverware lean
GRID_WP = [0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75]
GRID_SIGMA = [2.0, 3.0, 4.0, 5.0, 6.0]
GRID_GAP = [0.0, 2.0, 4.0, 6.0, 8.0]
BACKTEST_SIMS = 100
PREDICT_SIMS = 5000
SCENARIO_SIMS = 1500
WEIGHT_SCAN_SIMS = 200
OTHER = "Other nominee"


def criteria_scores(crit, year, overrides=None):
    tv = crit["trophy_values"]
    scores = {}
    for name, c in crit["years"][str(year)].items():
        ledger = c["ledger"]
        if overrides and name in overrides:
            ledger = [[label, kind, overrides[name].get(label, f)] for label, kind, f in ledger]
        scores[name] = {"P": c["P"], "T": team_success(ledger, tv), "F": c["F"]}
    return scores


def merit(s, wp):
    return wp * s["P"] + (1.0 - W_F - wp) * s["T"] + W_F * s["F"]


def backtest_field(scores, cands, wp, gap):
    top = sorted((merit(scores[c], wp) for c in cands), reverse=True)
    lead = (top[0] + top[1]) / 2.0 - gap
    return [lead - FIELD_STEP * r for r in range(FIELD_SIZE)]


def remainder_field(scores, cands, wp, offset):
    floor = min(merit(scores[c], wp) for c in cands)
    return [floor + offset - FIELD_STEP * r for r in range(REMAINDER_SIZE)]


def calibrate_remainder(jurors, players, cands, scores, history, wp, sigma):
    """Offset (vs the weakest named contender) at which the generic remainder
    collects REMAINDER_SHARE of all points."""
    extra, wp_j = jury_inputs(jurors, players, cands, history, wp)
    base = base_utilities(cands, scores, extra, wp_j)
    full = 67.0 * len(jurors)
    lo, hi = -15.0, 15.0
    for _ in range(14):
        mid = (lo + hi) / 2.0
        _, _, totals, _ = simulate(cands, base, remainder_field(scores, cands, wp, mid), sigma, 60, 5)
        share = 1.0 - statistics.fmean(sum(t) for t in totals) / full
        lo, hi = (mid, hi) if share < REMAINDER_SHARE else (lo, mid)
    return (lo + hi) / 2.0


def base_utilities(cands, scores, extra, wp_j):
    return [[merit(scores[c], wp_j[j]) + extra[j][i] for i, c in enumerate(cands)] for j in range(len(wp_j))]


def simulate(cands, base, field, sigma, sims, seed):
    """Monte Carlo of the jury.

    base[j][i] = juror j's noise-free utility for candidate i; field = generic
    utilities appended to every ballot. Returns per-juror expected points,
    per-juror first-place shares, per-sim totals, and the expected number of
    ballots with a generic player first.
    """
    rng = random.Random(seed)
    gauss = rng.gauss
    n, k = len(base), len(cands)
    m = k + len(field)
    exp_pts = [[0.0] * k for _ in range(n)]
    firsts = [[0] * k for _ in range(n)]
    totals = []
    field_firsts = 0
    for _ in range(sims):
        tot = [0] * k
        for j in range(n):
            util = [b + gauss(0.0, sigma) for b in base[j]] + [f + gauss(0.0, sigma) for f in field]
            order = sorted(range(m), key=util.__getitem__, reverse=True)
            if order[0] < k:
                firsts[j][order[0]] += 1
            else:
                field_firsts += 1
            row = exp_pts[j]
            for pos in range(10):
                i = order[pos]
                if i < k:
                    pts = points_for(pos + 1)
                    tot[i] += pts
                    row[i] += pts
        totals.append(tot)
    exp_pts = [[v / sims for v in row] for row in exp_pts]
    first_share = [[v / sims for v in row] for row in firsts]
    return exp_pts, first_share, totals, field_firsts / sims


def chalk_ballots(cands, base, field):
    """Noise-free ballots: each juror's single most likely top 10 (names)."""
    names = cands + [OTHER] * len(field)
    out = []
    for row in base:
        util = row + field
        order = sorted(range(len(util)), key=util.__getitem__, reverse=True)
        out.append([names[i] for i in order[:10]])
    return out


def backtest(jurors, players, hist, crit):
    years = {}
    for year in (2024, 2025):
        cfg = hist[str(year)]
        active = [j for j in jurors if j["seat"] not in cfg["excluded_seats"]]
        cands = cfg["top3"]
        scores = criteria_scores(crit, year)
        scores = {c: scores[c] for c in cands}
        extra = [[bloc_affinity(j, players, c, year) for c in cands] for j in active]
        years[year] = (cfg, active, cands, scores, extra)

    def score(wp, sigma, gap, sims):
        loss, detail = 0.0, {}
        for year, (cfg, active, cands, scores, extra) in years.items():
            base = base_utilities(cands, scores, extra, [wp] * len(active))
            field = backtest_field(scores, cands, wp, gap)
            exp_pts, first_share, totals, field_first = simulate(cands, base, field, sigma, sims, seed=year)
            pred_tot = [sum(row[i] for row in exp_pts) for i in range(3)]
            pred_first = [sum(row[i] for row in first_share) for i in range(3)]
            act_first = [cfg["firsts"][c] for c in cands]
            act_field = len(active) - sum(act_first)
            wins = sum(1 for t in totals if max(range(3), key=t.__getitem__) == 0)
            for i, c in enumerate(cands):
                loss += ((pred_tot[i] - cfg["totals"][c]) / 50.0) ** 2
                loss += ((pred_first[i] - act_first[i]) / 5.0) ** 2
            loss += ((field_first - act_field) / 5.0) ** 2
            detail[year] = {
                "cands": cands, "pred_tot": pred_tot, "pred_first": pred_first,
                "act_tot": [cfg["totals"][c] for c in cands], "act_first": act_first,
                "pred_field_first": field_first, "act_field_first": act_field,
                "p_actual_winner_wins": wins / sims,
            }
        return loss, detail

    grid = []
    for wp in GRID_WP:
        for sigma in GRID_SIGMA:
            for gap in GRID_GAP:
                loss, _ = score(wp, sigma, gap, BACKTEST_SIMS)
                grid.append((loss, wp, sigma, gap))
    grid.sort()
    _, wp, sigma, gap = grid[0]
    loss, detail = score(wp, sigma, gap, 1000)
    return {"wP": wp, "wT": round(1.0 - W_F - wp, 2), "wF": W_F, "sigma": sigma, "gap": gap,
            "loss": loss, "detail": detail, "grid": grid}


def juror_history(jurors, cands):
    """Per-juror z-score of past points for each candidate, plus output-vs-silverware lean.

    A candidate's history uses every year in which he was tracked in the
    rebuilt ballots; candidates never tracked get 0 for every juror.
    """
    years = {}
    for year in (2024, 2025):
        rows = read_csv(os.path.join(OUT, f"ballots_{year}.csv"))
        years[year] = {int(r["seat"]): r for r in rows}
    z, lean = {}, {}
    for c in cands:
        col = f"{c} pts"
        past = {}
        for j in jurors:
            vals = [int(rows[j["seat"]][col]) for rows in years.values()
                    if col in rows[j["seat"]] and rows[j["seat"]]["source"] != "no ballot"]
            if vals:
                past[j["seat"]] = statistics.fmean(vals)
        mu = statistics.fmean(past.values()) if past else 0.0
        sd = (statistics.pstdev(past.values()) if len(past) > 1 else 0.0) or 1.0
        for j in jurors:
            z.setdefault(j["seat"], {})[c] = (past[j["seat"]] - mu) / sd if j["seat"] in past else 0.0
    for j in jurors:
        r24, r25 = years[2024][j["seat"]], years[2025][j["seat"]]
        leans = [(int(r25["Lamine Yamal pts"]) - int(r25["Vitinha pts"])) / 15.0]
        if r24["source"] != "no ballot":
            leans.append((int(r24["Vinícius Júnior pts"]) - int(r24["Rodri pts"])) / 15.0)
        lean[j["seat"]] = statistics.fmean(leans)
    return z, lean


def jury_inputs(jurors, players, cands, history, wp, use_history=True):
    """Per-juror affinity+history offsets and personal wP."""
    z, lean = history
    extra, wp_j = [], []
    for j in jurors:
        s = j["seat"]
        extra.append([bloc_affinity(j, players, c, 2026) + (HISTORY_GAMMA * z[s][c] if use_history else 0.0)
                      for c in cands])
        shift = LEAN_BETA * lean[s] if use_history else 0.0
        wp_j.append(min(1.0 - W_F, max(0.0, wp + shift)))
    return extra, wp_j


def run_2026(jurors, players, cands, scores, history, wp, sigma, offset, sims, seed, use_history=True):
    extra, wp_j = jury_inputs(jurors, players, cands, history, wp, use_history)
    base = base_utilities(cands, scores, extra, wp_j)
    field = remainder_field(scores, cands, wp, offset)
    exp_pts, first_share, totals, field_first = simulate(cands, base, field, sigma, sims, seed)
    wins = [0] * len(cands)
    for t in totals:
        wins[max(range(len(cands)), key=t.__getitem__)] += 1
    return {
        "exp_pts": exp_pts, "first_share": first_share, "totals": totals, "field_first": field_first,
        "win_prob": [w / sims for w in wins], "chalk": chalk_ballots(cands, base, field),
        "mean": [statistics.fmean(t[i] for t in totals) for i in range(len(cands))],
    }


def structural_win_prob(jurors, players, cands, crit, fit, history, offset, draws=2000, seed=7):
    """Win probability once the model's own assumptions are uncertain too.

    Each draw picks (wP, sigma) from the backtest grid in proportion to
    exp(-loss/2), nudges every P score by N(0, 2) and every T score by +/-10%,
    then simulates one jury.
    """
    rng = random.Random(seed)
    grid = fit["grid"]
    best = grid[0][0]
    weights = [pow(2.718281828, -(loss - best) / 2.0) for loss, *_ in grid]
    base_scores = criteria_scores(crit, 2026)
    wins = [0] * len(cands)
    for d in range(draws):
        _, wp, sigma, _ = rng.choices(grid, weights)[0]
        scores = {c: {"P": s["P"] + rng.gauss(0.0, 2.0), "T": s["T"] * (1.0 + rng.gauss(0.0, 0.10)), "F": s["F"]}
                  for c, s in base_scores.items()}
        r = run_2026(jurors, players, cands, scores, history, wp, sigma, offset, 1, seed + d)
        t = r["totals"][0]
        wins[max(range(len(cands)), key=t.__getitem__)] += 1
    return [w / draws for w in wins]


def pct(values, q):
    v = sorted(values)
    return v[min(len(v) - 1, int(q * len(v)))]


def top3(cands, means):
    order = sorted(range(len(cands)), key=lambda i: -means[i])[:3]
    return [[cands[i], means[i]] for i in order]


def main():
    jurors = load_jurors()
    players = load_json("players.json")
    hist = load_json("history.json")
    crit = load_json("criteria.json")
    scores = criteria_scores(crit, 2026)
    cands = list(scores)

    fit = backtest(jurors, players, hist, crit)
    print(f"fitted: wP={fit['wP']} wT={fit['wT']} wF={fit['wF']} sigma={fit['sigma']} gap={fit['gap']}")
    rows = []
    for year, d in fit["detail"].items():
        for i, c in enumerate(d["cands"]):
            rows.append([year, c, d["act_tot"][i], round(d["pred_tot"][i]), d["act_first"][i], round(d["pred_first"][i], 1)])
        print(f"  {year}: actual winner wins in {d['p_actual_winner_wins']:.0%} of simulated juries")
    write_csv(os.path.join(OUT, "backtest.csv"),
              ["year", "player", "actual_points", "model_points", "actual_first_places", "model_first_places"], rows)

    history = juror_history(jurors, cands)
    offset = calibrate_remainder(jurors, players, cands, scores, history, fit["wP"], fit["sigma"])
    base = run_2026(jurors, players, cands, scores, history, fit["wP"], fit["sigma"], offset, PREDICT_SIMS, 2026)
    overall = structural_win_prob(jurors, players, cands, crit, fit, history, offset)

    order = sorted(range(len(cands)), key=lambda i: -base["mean"][i])
    chalk_pts = [0] * len(cands)
    chalk_first = [0] * len(cands)
    for ballot in base["chalk"]:
        for pos, name in enumerate(ballot, 1):
            if name in scores:
                chalk_pts[cands.index(name)] += points_for(pos)
        if ballot[0] in scores:
            chalk_first[cands.index(ballot[0])] += 1
    board = []
    for rank, i in enumerate(order, 1):
        c = cands[i]
        s = scores[c]
        col = [t[i] for t in base["totals"]]
        board.append({
            "rank": rank, "player": c, "P": s["P"], "T": round(s["T"], 1), "F": s["F"],
            "merit": round(merit(s, fit["wP"]), 1), "points": base["mean"][i],
            "p05": pct(col, 0.05), "p95": pct(col, 0.95),
            "firsts": sum(r[i] for r in base["first_share"]), "chalk_points": chalk_pts[i],
            "chalk_firsts": chalk_first[i], "win_noise": base["win_prob"][i], "win_overall": overall[i],
        })
    write_csv(os.path.join(OUT, "prediction_2026_leaderboard.csv"),
              ["rank", "player", "P", "T", "F", "merit", "projected_points", "p05", "p95", "expected_first_places",
               "predicted_ballot_points", "predicted_ballot_first_places", "win_prob_juror_noise", "win_prob_overall"],
              [[b["rank"], b["player"], b["P"], b["T"], b["F"], b["merit"], round(b["points"]), b["p05"], b["p95"],
                round(b["firsts"], 1), b["chalk_points"], b["chalk_firsts"], round(b["win_noise"], 3),
                round(b["win_overall"], 3)] for b in board])

    write_csv(os.path.join(OUT, "prediction_2026_ballots.csv"),
              ["seat", "country", "juror", "confed"] + [f"{p}{'st' if p == 1 else 'nd' if p == 2 else 'rd' if p == 3 else 'th'}"
                                                        for p in range(1, 11)],
              [[j["seat"], j["country"], j["juror"], j["confed"]] + base["chalk"][n] for n, j in enumerate(jurors)])
    ranked = [cands[i] for i in order]
    write_csv(os.path.join(OUT, "prediction_2026_expected_points.csv"),
              ["seat", "country", "juror"] + ranked + [f"P(1st) {c}" for c in ranked[:5]],
              [[j["seat"], j["country"], j["juror"]] + [round(base["exp_pts"][n][i], 1) for i in order]
               + [round(base["first_share"][n][i], 2) for i in order[:5]] for n, j in enumerate(jurors)])

    scenarios = [
        ("Baseline (fitted weights)", {}),
        ("Silverware-heavy jury (wP = wT = 0.45)", {"wp": 0.45}),
        ("Output-heavy jury (wP + 0.05)", {"wp": fit["wP"] + 0.05}),
        ("Yamal rated Spain's World Cup standout (essential 1.0)",
         {"overrides": {"Lamine Yamal": {"World Cup winner": 1.0}}}),
        ("No juror history (merit + blocs only)", {"use_history": False}),
    ]
    sens = []
    for label, kw in scenarios:
        if not kw:
            means = base["mean"]
        else:
            sc = criteria_scores(crit, 2026, kw.get("overrides"))
            r = run_2026(jurors, players, cands, sc, history, kw.get("wp", fit["wP"]), fit["sigma"], offset,
                         SCENARIO_SIMS, 2026, kw.get("use_history", True))
            means = r["mean"]
        sens.append({"label": label, "top3": top3(cands, means)})
        print(f"  {label}: " + ", ".join(f"{c} {m:.0f}" for c, m in top3(cands, means)))

    weight_scan = []
    for step in range(0, 31):
        wp = round(0.45 + step / 100.0, 2)
        r = run_2026(jurors, players, cands, scores, history, wp, fit["sigma"], offset, WEIGHT_SCAN_SIMS, 11)
        weight_scan.append({"wP": wp, "top3": top3(cands, r["mean"])})
    bands = []
    for row in weight_scan:
        leader = row["top3"][0][0]
        if bands and bands[-1]["leader"] == leader:
            bands[-1]["to"] = row["wP"]
        else:
            bands.append({"leader": leader, "from": row["wP"], "to": row["wP"]})

    summary = {
        "fit": {k: v for k, v in fit.items() if k not in ("detail", "grid")},
        "backtest": fit["detail"],
        "leaderboard": board,
        "field_first_expected": base["field_first"],
        "remainder_points": 67 * len(jurors) - sum(b["points"] for b in board),
        "remainder_offset": offset,
        "sensitivity": sens,
        "weight_scan": [w for w in weight_scan if round(w["wP"] * 100) % 5 == 0],
        "leader_bands": bands,
        "params": {"W_F": W_F, "REMAINDER_SIZE": REMAINDER_SIZE, "REMAINDER_SHARE": REMAINDER_SHARE,
                   "FIELD_SIZE": FIELD_SIZE, "FIELD_STEP": FIELD_STEP, "HISTORY_GAMMA": HISTORY_GAMMA,
                   "LEAN_BETA": LEAN_BETA, "PREDICT_SIMS": PREDICT_SIMS},
    }
    with open(os.path.join(OUT, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    for b in board:
        print(f"{b['rank']:2d}. {b['player']:24s} {b['points']:6.0f} pts  1st x{b['firsts']:4.1f}  "
              f"win {b['win_overall']:.0%}")
    print("leader by wP: " + "; ".join(f"{b['from']}-{b['to']}: {b['leader']}" for b in bands))


if __name__ == "__main__":
    main()
