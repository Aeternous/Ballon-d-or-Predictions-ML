"""Shared helpers: ballot points, jury roster, player tags and bloc affinity."""

import csv
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "output")

# Official ballot: 10 places, 15-12-10-8-7-5-4-3-2-1.
POINTS = (15, 12, 10, 8, 7, 5, 4, 3, 2, 1)
MAX_PER_BALLOT = POINTS[0]

# Bloc affinity sizes, in utility points on the 0-100 criteria scale.
AFFINITY = {
    "home": 5.0,         # juror's country == player's country
    "nat_lang": 1.5,     # juror's media bloc == player's national language bloc
    "league_lang": 1.0,  # juror's media bloc == language of the league the player plays in
}


def points_for(position):
    """Points for a 1-based ballot position; 0 when off the ballot."""
    if position and 1 <= position <= len(POINTS):
        return POINTS[position - 1]
    return 0


def load_json(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


def load_jurors():
    with open(os.path.join(DATA, "jurors.csv"), encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row["seat"] = int(row["seat"])
        row["langs"] = set(row["langs"].split("|"))
    return rows


def player_tags(players, name, year):
    """(nation, nat_lang, league_lang) for a player; generic nominees have no tags."""
    info = players.get(name)
    if info is None:
        return None, None, None
    league = info["league_lang"]
    if isinstance(league, dict):
        league = league[str(year)]
    return info["nation"], info["nat_lang"], league


def bloc_affinity(juror, players, name, year):
    nation, nat_lang, league_lang = player_tags(players, name, year)
    if nation is None:
        return 0.0
    a = 0.0
    if juror["country"] == nation:
        a += AFFINITY["home"]
    if nat_lang in juror["langs"]:
        a += AFFINITY["nat_lang"]
    if league_lang in juror["langs"]:
        a += AFFINITY["league_lang"]
    return a


def team_success(ledger, trophy_values):
    """T score: sum of trophy value x essential factor, capped at 100."""
    return min(100.0, sum(trophy_values[kind] * factor for _, kind, factor in ledger))


def write_csv(path, header, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))
