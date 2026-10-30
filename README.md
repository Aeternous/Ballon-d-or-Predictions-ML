# Ballon d'Or 2026 juror model

Predicts how each of the 100 Ballon d'Or jurors will fill their 2026 ballot across **17 named contenders**: Kane, Yamal, Mbappé, Messi, Kvaratskhelia, Rodri, Bruno Fernandes, Rice, Haaland, Bellingham, Lautaro, Luis Díaz, Olise, Nuno Mendes, Dembélé, Vinícius and Vitinha. It first rebuilds how the same jury seats scored the 2024 (Rodri, Vinícius, Bellingham) and 2025 (Dembélé, Yamal, Vitinha) races.

**Read the results in [`output/REPORT.md`](ballon-dor-2026/output/REPORT.md).**

## Pipeline

| Step | Script | Output |
|---|---|---|
| 1. Rebuild 2024/2025 ballots so they match every published total, first-place count and verified ballot | `src/reconstruct.py` | `output/ballots_2024.csv`, `output/ballots_2025.csv` |
| 2. Fit the criteria weights on 2024/2025, then simulate the 2026 jury | `src/predict.py` | `output/backtest.csv`, `output/prediction_2026_leaderboard.csv`, `output/prediction_2026_ballots.csv` (each juror's predicted top 10), `output/prediction_2026_expected_points.csv`, `output/summary.json` |
| 3. Write the report | `src/report.py` | `output/REPORT.md` |

```
cd src && python3 reconstruct.py && python3 predict.py && python3 report.py
```

Python 3 standard library only; seeds are fixed, so reruns reproduce the same numbers.

## Inputs

- `data/jurors.csv`: the 100-seat jury roster, with confederation, media-language bloc and notes where the roster differs from who actually voted.
- `data/history.json`: published 2024/2025 totals, first-place splits and verified individual ballots, with sources.
- `data/criteria.json`: scores for the three official criteria (Individual Performance, Team Success via a trophy ledger, Fair Play) for every candidate-year. Every player listed under `2026` is modelled by name; add or remove players there, or change scores to test your own view.
- `data/players.json`: nationality and league tags used for juror affinity.
