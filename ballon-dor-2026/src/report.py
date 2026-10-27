"""Build output/REPORT.md from the data files and the model outputs."""

import json
import os
import statistics
from collections import defaultdict

from common import OUT, load_json, load_jurors, read_csv, team_success

CONFEDS = ["UEFA", "CONMEBOL", "CONCACAF", "CAF", "AFC", "OFC"]

SOURCES = [
    ("2024 points totals (90min)", "https://www.90min.com/ballon-dor-2024-full-points-totals-revealed"),
    ("2024 voting breakdown, first places by country (GOAL)", "https://www.goal.com/en-us/lists/full-2024-ballon-dor-voting-breakdown-reveals-rodri-margin-victory-over-vinicius-jr-controversial-contest/blt0e0bff7ed05adce4"),
    ("2024 France juror's ballot (GOAL France)", "https://www.goal.com/fr/listes/ballon-d-or-2024-le-vote-surprenant-de-la-france-et-les-points-detailles-des-joueurs/bltdcb101478c4b27e8"),
    ("2024 every journalist's vote (GiveMeSport)", "https://www.givemesport.com/journalist-votes-2024-ballon-dor-rodri-vinicius-bellingham/"),
    ("2024 African jurors' first places (allAfrica)", "https://fr.allafrica.com/stories/202411090289.html"),
    ("2024 Ghana juror, Rodri ahead of Vinícius", "https://turn.liquiddesign.co.uk/sports/football/270826-michael-oti-adjei-how-ghanaian-journalist-voted-2024-ballon-d-rodri-vini"),
    ("2024 jurors who left Vinícius out (Finland, El Salvador, Namibia)", "https://element.liquiddesign.co.uk/sports/football/270842-finnish-journalist-resigns-ballon-d-jury-mistake-voting-vinicius-junior"),
    ("2025 points totals (World Soccer Talk)", "https://worldsoccertalk.com/news/2025-ballon-dor-voting-results-revealed-how-close-were-ousmane-dembele-and-lamine-yamal-how-many-points-did-mohamed-salah-and-kylian-mbappe-receive/"),
    ("2025 positions 11-30 (Foot Africa)", "https://foot-africa.com/en/news/ballon-dor-2025-full-voting-breakdown-revealed-895881/"),
    ("2025 first-place counts (Sports Illustrated)", "https://www.si.com/soccer/2025-ballon-dor-voting-breakdown-revealed"),
    ("2025 how each country voted (Tribuna)", "https://tribuna.com/en/blogs/how-each-country-voted-for-in-2025-ballon-dor-revealed/"),
    ("2025 country votes incl. Georgia/Scotland (Sportaran)", "https://sportaran.com/en/post/kak-golosovali-strany-za-zolotoj-myach-2025-raskryty-rezultaty-ballon-dor/"),
    ("2025 Spain juror's top 3 (SPORTbible)", "https://www.sportbible.com/football/football-news/ballon-dor-ousmane-dembele-lamine-yamal-psg-barcelona-716363-20250923"),
    ("2025 Ghana juror's ballot (Flashscore)", "https://www.flashscore.com/news/soccer-champions-league-how-ghana-s-journalist-voted-in-the-2025-ballon-d-or-awards/QPbVqrCk"),
    ("2025 South Africa juror's ballot (Sportsclub)", "https://www.sportsclub.co.za/?p=224719"),
    ("Kane 2025/26 numbers (Bundesliga.com)", "https://www.bundesliga.com/en/bundesliga/news/harry-kane-2025-26-numbers-england-bauern-munich-goals-records-messi-38301"),
    ("Bayern win the 2026 DFB-Pokal final (FC Bayern)", "https://fcbayern.com/en/matches/profis/dfb-pokal/2025-2026/fc-bayern-muenchen-vfb-stuttgart-23-05-2026/report"),
    ("Bayern out to PSG in the UCL semi-final (Bundesliga.com)", "https://www.bundesliga.com/en/bundesliga/news/bayern-munich-manuel-neuer-killer-instinct-champions-league-final-psg-37259"),
    ("Yamal, LaLiga 2025/26 Player of the Season (FC Barcelona)", "https://www.fcbarcelona.com/en/football/first-team/news/4514485/lamine-yamal-202526-laliga-player-of-the-season"),
    ("Yamal out for the rest of the club season (AP)", "https://www.clickorlando.com/sports/2026/04/23/yamal-to-miss-rest-of-barcelona-season-but-be-fit-for-world-cup-with-spain/"),
    ("Barcelona out to Atlético in the UCL quarter-final (theScore)", "https://thescore.com/news/3523183"),
    ("Mbappé wins the 2025/26 Pichichi (Real Madrid)", "https://www.realmadrid.com/en-US/news/football/first-team/latest-news/mbappe-gana-el-trofeo-pichichi-2025-26-23-05-2026"),
    ("Mbappé 2025/26 UCL top scorer (Real Madrid)", "https://www.realmadrid.com/en-US/news/football/first-team/latest-news/mbappe-recibe-el-premio-al-maximo-goleador-de-la-champions-league-2025-26-08-09-2026"),
    ("Real Madrid out to Bayern in the UCL quarter-final (GOAL)", "https://www.goal.com/en-sg/lists/jude-bellingham-speaks-out-real-madrid-controversial-champions-league-exit/bltf4ec2b542d3ca9be"),
    ("World Cup final: Spain 1-0 Argentina; Rodri Golden Ball; Mbappé Golden Boot (TSN)", "https://www.tsn.ca/soccer/fifa-world-cup/article/frances-mbappe-wins-2026-fifa-world-cup-golden-boot/"),
    ("France out to Spain in the World Cup semi-final (Yahoo Sports)", "https://sports.yahoo.com/articles/france-eliminated-world-cup-heartbreaking-205427061.html"),
    ("England beat France 6-4 for World Cup 3rd place (Euronews)", "https://euronews.com/2026/07/19/england-beat-france-6-4-in-world-cup-third-place-thriller"),
    ("2026 UCL final: PSG beat Arsenal on penalties (Wikipedia)", "https://en.wikipedia.org/wiki/2026_UEFA_Champions_League_final"),
    ("Ballon d'Or 2026 odds, 29 Sep 2026 (Oddschecker)", "https://www.oddschecker.com/insight/football/20260929-ballon-dor-2026-odds-harry-kane-favourite-ahead-of-lamine-yamal"),
    ("Arsenal crowned 2025/26 Premier League champions (Arsenal)", "https://www.arsenal.com/news/arsenal-crowned-202526-premier-league-champions"),
    ("Man City win the 2026 FA Cup (The FA)", "https://www.thefa.com/news/2026/may/16/emirates-fa-cup-final-chelsea-v-manchester-city-report-20261605"),
    ("Man City exit the UCL in the last 16 (Premier League)", "https://www.premierleague.com/en/news/4250621"),
    ("Inter out of the UCL to Bodø/Glimt (Inter)", "https://www.inter.it/en/news/inter-bodo-glimt-champions-league-2025-2026"),
    ("Lautaro, Serie A 2025/26 top scorer (Inter)", "https://www.inter.it/en/news/lautaro-martinez-top-scorer-serie-a-2025-26"),
    ("World Cup knockout results (FIFA)", "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/knockout-stage-match-schedule-bracket"),
    ("Portugal out to Spain in the World Cup last 16 (NBC)", "https://www.nbcdfw.com/world-cup/spain-portugal-score-cristiano-ronaldo/4045474/"),
    ("Colombia out to Switzerland in the World Cup last 16 (FC Bayern)", "https://fcbayern.com/en/news/2026/07/luis-diaz-colombia-miss-out-on-world-cup-quarter-finals"),
    ("Rodri wins the World Cup Golden Ball (FIFA)", "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/rodri-earns-adidas-golden-ball"),
    ("Messi: Silver Ball and Silver Boot (LatestLY)", "https://www.latestly.com/sports/football/lionel-messi-wins-silver-ball-and-silver-boot-at-fifa-world-cup-2026-awards-7523924.html"),
    ("Messi named MLS Cup 2025 MVP (MLS)", "https://www.mlssoccer.com/news/inter-miami-s-lionel-messi-named-mls-cup-2025-mvp-pres-by-audi"),
    ("Kvaratskhelia, 2025/26 UCL Player of the Season (UEFA)", "https://www.uefa.com/uefachampionsleague/news/02a5-20c1d7bf915e-f9e703cf0108-1000--khvicha-kvaratskhelia-named-2025-26-uefa-champions-league-/"),
    ("Why Kvaratskhelia missed the World Cup (World Soccer Talk)", "https://worldsoccertalk.com/world-cup/why-khvicha-kvaratskhelia-is-not-playing-in-the-2026-world-cup"),
    ("Vitinha, 2026 UCL final Player of the Match (UEFA)", "https://www.uefa.com/uefachampionsleague/news/02a5-20c0324a93c4-a269d65f5aeb-1000--vitinha-named-official-2026-uefa-champions-league-final-play/"),
    ("PSG win the 2025 UEFA Super Cup (beIN)", "https://www.beinsports.com/en-us/soccer/uefa-super-cup/articles/psg-pulls-off-historic-comeback-against-tottenham-to-win-the-uefa-super-cup-2025-08-13"),
    ("PSG win the 2025 Intercontinental Cup (FIFA)", "https://www.fifa.com/en/tournaments/mens/intercontinentalcup/2025/articles/paris-saint-germain-flamengo-match-report"),
    ("PSG win the 2026 Trophée des Champions (PSG)", "https://www.psg.fr/en/content/match-report-paris-saint-germain-olympique-de-marseille-trophee-des-champions-kuwait-city-2025"),
    ("Dembélé 2026 World Cup hat-trick vs Norway (Al Jazeera)", "https://www.aljazeera.com/sports/2026/6/26/dembele-scores-hat-trick-as-france-beat-norway-4-1-at-world-cup-2026"),
    ("Haaland scores twice to knock out Brazil (Al Jazeera)", "https://www.aljazeera.com/sports/2026/7/5/haaland-scores-twice-as-norway-stun-brazil-2-1-in-world-cup-2026-last-16"),
    ("Bellingham's England major-tournament goal record (England Football)", "https://www.englandfootball.com/articles/2026/Jul/18/jude-bellingham-major-tournament-record-scorer-england-20261807"),
    ("Declan Rice captains England in the bronze match (England Football)", "https://www.englandfootball.com/articles/2026/Jul/19/declan-rice-france-england-captaincy-stats-20261907"),
    ("Bruno Fernandes breaks the Premier League assist record (beIN)", "https://www.beinsports.com/en-us/soccer/premier-league/articles/bruno-fernandes-breaks-historic-premier-league-assist-record-2026-05-24"),
    ("Luis Díaz 2025/26: 24 goals, 17 assists (Sofascore)", "https://www.sofascore.com/news/elite-output-little-noise-luis-diazs-bayern-season-in-numbers"),
    ("Olise, Bundesliga 2025/26 Player of the Season (Bundesliga.com)", "https://www.bundesliga.com/en/bundesliga/news/player-of-the-month-2025-26-vote-winners-ea-sports-olise-34233"),
    ("Ballon d'Or 2026 30-man shortlist (Yen)", "https://yen.com.gh/sports/football/311547-ballon-d-2026-full-list-30-man-nominees-lamine-yamal-mbappe-head-head/"),
]

MARKET = {"Harry Kane": ("5/4", 4 / 9), "Lamine Yamal": ("2/1", 1 / 3), "Kylian Mbappé": ("14/1", 1 / 15)}


def short(name):
    return {"Vinícius Júnior": "Vinícius", "Jude Bellingham": "Bellingham", "Ousmane Dembélé": "Dembélé",
            "Lamine Yamal": "Yamal", "Kylian Mbappé": "Mbappé", "Harry Kane": "Kane", "Khvicha Kvaratskhelia": "Kvaratskhelia",
            "Lionel Messi": "Messi", "Michael Olise": "Olise", "Luis Díaz": "Díaz", "Erling Haaland": "Haaland",
            "Lautaro Martínez": "Lautaro", "Nuno Mendes": "N. Mendes", "Declan Rice": "Rice", "Bruno Fernandes": "Bruno",
            "Other nominee": "other"}.get(name, name)


def pts(v):
    return "–" if v in ("", None) else str(v)


def year_section(year, hist, jurors):
    cfg = hist[str(year)]
    rows = read_csv(os.path.join(OUT, f"ballots_{year}.csv"))
    top3 = cfg["top3"]
    conf = {j["seat"]: j["confed"] for j in jurors}
    voters = [r for r in rows if r["source"] != "no ballot"]
    lines = [f"## {year}: how the jury scored the top 3", ""]
    lines.append(f"Winner: **{cfg['winner']}**. Jury: {cfg['jury_size']} ballots. "
                 f"First places are published counts. Points by confederation and by juror come from the rebuilt ballots, "
                 f"which add up exactly to the published totals.")
    lines.append("")
    lines.append("| Player | Total points | First places | Avg per ballot | Avg UEFA | Avg CONMEBOL | Avg CONCACAF | Avg CAF | Avg AFC | Avg OFC |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for p in top3:
        by = defaultdict(list)
        for r in voters:
            by[conf[int(r["seat"])]].append(int(r[f"{p} pts"]))
        tot = sum(int(r[f"{p} pts"]) for r in voters)
        cells = [f"{statistics.fmean(by[c]):.1f}" if by[c] else "–" for c in CONFEDS]
        label = f"**{p}** (winner)" if p == cfg["winner"] else p
        lines.append(f"| {label} | {tot} | {cfg['firsts'][p]} | {tot / len(voters):.1f} | " + " | ".join(cells) + " |")
    lines.append("")
    counts = defaultdict(int)
    for r in voters:
        counts[r["source"]] += 1
    lines.append(f"Ballot sources: {counts['verified']} verified, {counts['partial']} partly verified "
                 f"(e.g. only the 1st place is published), {counts['reconstructed']} rebuilt by the model.")
    lines.append("")
    lines.append(f"<details><summary>All {len(rows)} jurors: points given to {', '.join(short(p) for p in top3)} in {year}</summary>")
    lines.append("")
    head = "| # | Country | Juror (your roster) | " + " | ".join(f"{short(p)} pos" for p in top3) + " | " \
        + " | ".join(f"{short(p)} pts" for p in top3) + " | Their 1st place | Source |"
    lines.append(head)
    lines.append("|" + "---|" * (3 + 2 * len(top3) + 2))
    for r in rows:
        cells = [r["seat"], r["country"], r["juror"]]
        cells += [pts(r[f"{p} pos"]) for p in top3]
        cells += [r[f"{p} pts"] if r["source"] != "no ballot" else "–" for p in top3]
        cells += [r["first_place"] or "–", r["source"]]
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    lines.append("</details>")
    lines.append("")
    return lines


def criteria_section(crit):
    tv = crit["trophy_values"]
    lines = ["## Criteria scores fed to the model", "",
             "P = Individual Performance, Decisiveness & Impressive Character. "
             "T = Team Success (trophy value × how essential the player was, capped at 100). "
             "F = Class & Fair Play. All on 0–100.", "",
             "| Year | Player | P | T | F | Basis |", "|---|---|---:|---:|---:|---|"]
    for year in ("2024", "2025", "2026"):
        for name, c in crit["years"][year].items():
            t = team_success(c["ledger"], tv)
            trophies = "; ".join(f"{label} ×{f}" for label, _, f in c["ledger"])
            lines.append(f"| {year} | {name} | {c['P']} | {t:.1f} | {c['F']} | {c['P_note']}. Silverware: {trophies}. {c['F_note']}. |")
    lines.append("")
    return lines


def prediction_section(summary, jurors):
    board = summary["leaderboard"]
    fit = summary["fit"]
    lb = {b["player"]: b for b in board}
    lines = [f"## 2026 prediction: all {len(board)} contenders", ""]
    podium = board[:3]
    lines.append(f"**Predicted winner: {podium[0]['player']}**, then {podium[1]['player']} and {podium[2]['player']}.")
    lines.append("")
    lines.append("| # | Player | P | T | F | Projected points | 90% range | Expected 1st places | Predicted-ballot points | Win probability | Bookmakers, 29 Sep |")
    lines.append("|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|")
    for b in board:
        mk = MARKET.get(b["player"])
        mk_s = f"{mk[0]} (~{mk[1]:.0%})" if mk else "–"
        lines.append(f"| {b['rank']} | {b['player']} | {b['P']} | {b['T']:.0f} | {b['F']} | **{b['points']:.0f}** | "
                     f"{b['p05']}–{b['p95']} | {b['firsts']:.1f} | {b['chalk_points']} | {b['win_overall']:.0%} | {mk_s} |")
    lines.append("")
    lines.append(f"- *Projected points* average 5,000 simulated juries. *Predicted-ballot points* score every juror's "
                 f"single most likely ballot, which exaggerates the leader's margin. *Win probability* also varies "
                 f"the criteria weights and every P/T score, not just juror-to-juror noise.")
    lines.append(f"- The other 13 shortlisted players you didn't list are modelled as a generic remainder. They are "
                 f"calibrated to take about {summary['params']['REMAINDER_SHARE']:.0%} of all points "
                 f"({summary['remainder_points']:.0f} here), the share places 18–30 took in 2025. "
                 f"They also take about {summary['field_first_expected']:.1f} first places.")
    lines.append("")
    lines.append("### Why the model lands here")
    lines.append("")
    k, d, kv, y, m = (lb[n] for n in ("Harry Kane", "Ousmane Dembélé", "Khvicha Kvaratskhelia", "Lamine Yamal", "Kylian Mbappé"))
    lines.append(f"- Fitted weights (backtest on 2024–25): Individual Performance **{fit['wP']:.2f}**, Team Success "
                 f"**{fit['wT']:.2f}**, Fair Play **{fit['wF']:.2f}**.")
    lines.append(f"- **Kane** has the highest individual score (P {k['P']}) by a distance. He scored 73 goals, won the "
                 f"Golden Shoe and the German double, and reached a Champions League semi-final and a World Cup semi-final.")
    lines.append(f"- **Dembélé, Kvaratskhelia and Yamal are a three-way race for 2nd**, spread over about {d['points'] - y['points']:.0f} points. "
                 f"The PSG pair have five trophies each (including the Champions League) on top of strong individual "
                 f"seasons. Yamal has the World Cup, but he scored once there and missed the end of the club season.")
    p_rank = 1 + sum(1 for b in board if b["P"] > m["P"])
    lines.append(f"- **Mbappé drops to #{m['rank']}.** His individual score (P {m['P']}) is #{p_rank} of {len(board)}. He won three "
                 f"scoring titles and the World Cup Bronze Ball. But with no trophy (T {m['T']:.0f}), 16 named rivals "
                 f"with silverware push him down most ballots. The bookmakers rate him far higher (3rd favourite).")
    r, me = lb["Rodri"], lb["Lionel Messi"]
    outside = max(board[4:], key=lambda b: b["firsts"])
    lines.append(f"- **Rodri** (World Cup Golden Ball) lands #{r['rank']} and **Messi** (Silver Ball, MLS Cup) #{me['rank']}. "
                 f"Outside the top four, {outside['player']} takes the most first places (about {outside['firsts']:.0f}).")
    lines.append("")
    lines.append("### Who leads at each weighting")
    lines.append("")
    bands = "; ".join(f"wP {b['from']:.2f}–{b['to']:.2f}: **{b['leader']}**" for b in summary["leader_bands"])
    lines.append(f"Leader as the weight on Individual Performance changes (Team Success = 0.90 − wP): {bands}.")
    lines.append("")
    lines.append("| wP | wT | 1st | 2nd | 3rd |")
    lines.append("|---:|---:|---|---|---|")
    for row in summary["weight_scan"]:
        t = row["top3"]
        lines.append(f"| {row['wP']:.2f} | {0.9 - row['wP']:.2f} | " + " | ".join(f"{c} ({p:.0f})" for c, p in t) + " |")
    lines.append("")
    lines.append("### Sensitivity")
    lines.append("")
    lines.append("| Scenario | 1st | 2nd | 3rd |")
    lines.append("|---|---|---|---|")
    for sc in summary["sensitivity"]:
        lines.append(f"| {sc['label']} | " + " | ".join(f"{c} ({p:.0f})" for c, p in sc["top3"]) + " |")
    lines.append("")

    exp_rows = read_csv(os.path.join(OUT, "prediction_2026_expected_points.csv"))
    top = [b["player"] for b in board[:6]]
    conf = {j["seat"]: j["confed"] for j in jurors}
    lines.append("### Projected points per ballot by confederation (top 6)")
    lines.append("")
    lines.append("| Confederation | Jurors | " + " | ".join(short(c) for c in top) + " |")
    lines.append("|---|---:|" + "---:|" * len(top))
    for cf in CONFEDS:
        rs = [r for r in exp_rows if conf[int(r["seat"])] == cf]
        lines.append(f"| {cf} | {len(rs)} | " + " | ".join(f"{statistics.fmean(float(r[c]) for r in rs):.1f}" for c in top) + " |")
    lines.append("")

    ballots = read_csv(os.path.join(OUT, "prediction_2026_ballots.csv"))
    exp_by_seat = {r["seat"]: r for r in exp_rows}
    lead4 = [b["player"] for b in board[:4]]
    lines.append("<details><summary>All 100 jurors: predicted 2026 ballot</summary>")
    lines.append("")
    lines.append("*1st–5th* is each juror's single most likely ballot (positions 6–10 are in "
                 "`output/prediction_2026_ballots.csv`). *P(1st)* is the chance that juror puts the player 1st, "
                 "across 5,000 simulated juries. Expected points for every juror and all 17 players are in "
                 "`output/prediction_2026_expected_points.csv`.")
    lines.append("")
    lines.append("| # | Country | Juror | 1st (15) | 2nd (12) | 3rd (10) | 4th (8) | 5th (7) | " +
                 " | ".join(f"P(1st) {short(c)}" for c in lead4) + " |")
    lines.append("|---|---|---|---|---|---|---|---|" + "---:|" * len(lead4))
    for r in ballots:
        e = exp_by_seat[r["seat"]]
        cells = [r["seat"], r["country"], r["juror"]] + [short(r[k]) for k in ("1st", "2nd", "3rd", "4th", "5th")]
        cells += [f"{float(e[f'P(1st) {c}']):.0%}" for c in lead4]
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    lines.append("</details>")
    lines.append("")
    return lines


def backtest_section(summary):
    fit = summary["fit"]
    lines = ["## Backtest: does the model reproduce 2024 and 2025?", "",
             f"Fitted on both years: wP = {fit['wP']}, wT = {fit['wT']}, wF = {fit['wF']}, "
             f"juror noise σ = {fit['sigma']}, field gap = {fit['gap']} (grid search; wP ≥ wT enforced).", "",
             "| Year | Player | Actual pts | Model pts | Actual 1st places | Model 1st places |",
             "|---|---|---:|---:|---:|---:|"]
    for year, d in summary["backtest"].items():
        for i, c in enumerate(d["cands"]):
            lines.append(f"| {year} | {c} | {d['act_tot'][i]} | {d['pred_tot'][i]:.0f} | {d['act_first'][i]} | {d['pred_first'][i]:.1f} |")
    lines.append("")
    d24, d25 = summary["backtest"]["2024"], summary["backtest"]["2025"]
    lines.append(f"The model picks Dembélé in {d25['p_actual_winner_wins']:.0%} of simulated 2025 juries. "
                 f"It picks Rodri in {d24['p_actual_winner_wins']:.0%} of simulated 2024 juries, and in the rest "
                 f"Vinícius edges it, which matches how close 2024 really was (41 points). "
                 f"It overrates Bellingham's 2024 first-place pull.")
    lines.append("")
    return lines


def main():
    jurors = load_jurors()
    hist = load_json("history.json")
    crit = load_json("criteria.json")
    with open(os.path.join(OUT, "summary.json"), encoding="utf-8") as f:
        summary = json.load(f)
    board = summary["leaderboard"]

    lines = ["# Ballon d'Or 2026: juror-by-juror prediction", ""]
    lines.append(f"**Model pick: {board[0]['player']}** ({board[0]['points']:.0f} projected points, "
                 f"{board[0]['win_overall']:.0%} win probability). Podium: "
                 + ", ".join(f"{b['player']} {b['points']:.0f}" for b in board[:3])
                 + f". {len(board)} contenders modelled by name.")
    lines.append("")
    lines.append("Voting closed on 28 September 2026. The award is presented on 26 October 2026.")
    lines.append("")
    lines.append("## Rules applied")
    lines.append("")
    lines.append("- Each of the 100 jurors ranks 10 players: 15, 12, 10, 8, 7, 5, 4, 3, 2, 1 points. The highest total wins.")
    lines.append("- Jurors weigh three criteria: (1) Individual Performance, Decisiveness & Impressive Character, "
                 "the highest-weighted; (2) Team Success, judged by how essential the player was to each trophy; "
                 "(3) Class & Fair Play, an ethical filter.")
    lines.append("- Award window: August to July, so 2026 covers the 2025/26 club season and the 2026 World Cup.")
    lines.append("")
    lines.append("## What is real and what is modelled")
    lines.append("")
    lines.append("- **Real:** every 2024 and 2025 points total, first-place count and regional split, plus the individual "
                 "ballots listed as *verified* or *partial* (France 2024; Spain, Ghana and South Africa 2025; first places for "
                 "England, Germany, Italy, Portugal, Netherlands, Brazil, Spain, Scotland, Slovenia, Ecuador; Finland and "
                 "El Salvador leaving Vinícius off in 2024). The 2025/26 stats and trophies behind every 2026 score are "
                 "sourced at the bottom.")
    lines.append("- **Rebuilt:** every other juror's 2024/2025 positions. France Football published the full sheet, but "
                 "it could not be fetched from this environment, so `reconstruct.py` rebuilds the most likely set of ballots "
                 "that reproduces every published number exactly. That includes the totals of every 2026 contender who "
                 "received votes in those years. Treat a *reconstructed* row as a model estimate, not as that journalist's actual vote.")
    lines.append("- **Judgment:** the P (individual) and F (fair play) scores and the 'how essential' trophy factors. "
                 "Each is written out below and can be edited in `data/criteria.json`.")
    lines.append("- **Roster:** the 100 jurors are the list you supplied. Some seats did not match the person who "
                 "actually voted (Portugal 2024, Ecuador 2024, El Salvador 2024, Spain 2025). Gabon, Honduras and Bolivia "
                 "appear twice. For 2024 (99 ballots) the second Gabon seat gets no ballot. See `data/jurors.csv`.")
    lines.append("")
    lines += year_section(2024, hist, jurors)
    lines += year_section(2025, hist, jurors)
    lines += criteria_section(crit)
    lines += backtest_section(summary)
    lines += prediction_section(summary, jurors)
    p = summary["params"]
    lines.append("## How each juror's 2026 ballot is modelled")
    lines.append("")
    lines.append("Utility for juror *j* and contender *c* = wP_j·P + wT_j·T + 0.10·F + bloc affinity + juror history + noise. "
                 "Each juror's ballot is the top 10 by utility.")
    lines.append("")
    lines.append("- **Bloc affinity:** +5 for the juror's own national players; +1.5 when the juror's media language "
                 "matches the player's nationality; +1.0 when it matches the league he plays in.")
    lines.append(f"- **Juror history:** +{p['HISTORY_GAMMA']} per standard deviation of the points that juror gave the same "
                 "player in the rebuilt 2024–25 ballots. Players who received no votes in those years (Messi, Bruno, "
                 "Díaz) get no history term.")
    lines.append(f"- **Output vs silverware lean:** jurors who put Vinícius above Rodri (2024) and Yamal above Vitinha (2025) "
                 f"get a slightly higher personal wP (±{p['LEAN_BETA']} per unit of lean).")
    lines.append(f"- **Unlisted nominees:** {p['REMAINDER_SIZE']} generic slots stand in for the other 13 shortlisted players. "
                 f"Their level is set so they take {p['REMAINDER_SHARE']:.0%} of all points.")
    lines.append("")
    lines.append("## Reproduce")
    lines.append("")
    lines.append("```")
    lines.append("cd ballon-dor-2026/src")
    lines.append("python3 reconstruct.py   # rebuild 2024/2025 ballots -> output/ballots_*.csv")
    lines.append("python3 predict.py       # backtest + 2026 simulation -> output/prediction_2026_*.csv, summary.json")
    lines.append("python3 report.py        # this report")
    lines.append("```")
    lines.append("")
    lines.append("Pure Python 3 standard library, fixed random seeds. Edit `data/criteria.json` to test your own scores, "
                 "or add or remove 2026 contenders there.")
    lines.append("")
    lines.append("## Sources")
    lines.append("")
    for label, url in SOURCES:
        lines.append(f"- [{label}]({url})")
    lines.append("")
    with open(os.path.join(OUT, "REPORT.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("wrote output/REPORT.md")


if __name__ == "__main__":
    main()
