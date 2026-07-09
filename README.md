# Iniesta vs Zidane: A Six-Dimensional Data Analysis

**Hypothesis**: Andres Iniesta is better than Zinedine Zidane.

## Methodology

Six pillars compared neutrally with no assigned weights:

| Pillar | Key Metrics |
|---|---|
| **Attack** | Goals, assists, xG, shot-creating actions per 90 |
| **Possession** | Pass completion %, progressive passes, dribble success |
| **Defense** | Pressures, tackles, interceptions, blocks per 90 |
| **Clutch** | Goals/assists in UCL KO, finals, World Cup KO, Euros KO |
| **Consistency** | Seasons at elite level, total minutes, peak duration |
| **Recognition** | Ballon d'Or, FIFPro XI, major honours, POTY awards |

Zidane played in the pre-analytics era (1989-2006) — advanced stats (xG, passing %, tackles) are estimated from historical records where unavailable. Iniesta played in the analytics era (2002-2024). All comparisons include context notes on this asymmetry.

Per-90 metrics are the primary comparison unit to account for different career lengths.

## Result

No single winner is declared. The comparison is presented neutrally across all six dimensions, each with full context and data-quality transparency.

| Pillar | Edge |
|---|---|
| **Attack** | Zidane (goalscoring) / Iniesta (creation) |
| **Possession** | Iniesta |
| **Defense** | Iniesta |
| **Clutch** | Draw |
| **Consistency** | Iniesta |
| **Recognition** | Zidane (individual awards) / Iniesta (team silverware) |

Zidane has the higher individual peak (Ballon d'Or 1998, World Cup final heroics, 3x FIFA World POTY). Iniesta has the greater longevity (885 matches, 16 elite seasons), superior possession metrics (90.5% pass completion), and more team honours (4 UCL, 9 La Liga, 9 FIFPro XI selections). Which dimension matters more is for the reader to decide.

## Files

| File | Description |
|---|---|
| `reports/iniesta-vs-zidane.html` | Self-contained HTML report with embedded charts |
| `notebooks/02-data-wrangling.ipynb` | Data processing and pillar construction |
| `notebooks/03-analysis.ipynb` | Analysis and all visualizations |
| `data/processed/six_pillars_dataset.csv` | Key metrics for both players |
| `data/processed/player_seasons.csv` | Per-season data |

## Data Sources

- Wikipedia (club + international career tables)
- StatsBomb (event data for Iniesta peak seasons)
- Transfermarkt (auxiliary match data)
- Manual compilation (trophies, awards, clutch records)

## Built With

Python, pandas, matplotlib. July 2026.
