# Iniesta vs Zidane — Data Analysis Project

**Hypothesis**: Andrés Iniesta is better than Zinedine Zidane.
**Approach**: Let data decide neutrally across six dimensions.
**Framework**: Python Jupyter notebooks, clean minimal visualizations.

---

## Project Status

- [x] Phase 1: Knowledge Base (skills + agents) — DONE
- [x] Phase 2: Data Collection — PARTIAL (Wikipedia scraped, FBref blocked by Cloudflare, manual fallback in place)
- [x] Phase 3: Data Wrangling — DONE
- [x] Phase 4: Analysis — DONE
- [x] Phase 5: Report — DONE

---

## Skills Created (in `.opencode/skills/`)

| Skill | Source | Purpose |
|---|---|---|
| `statistical-modeling` | Soccermatics (Sumpter) | Poisson, networks, flow fields, clustering, Markov chains |
| `xg-model` | Expected Goals Philosophy (Tippett) | xG estimation, finishing efficiency, xG chain |
| `player-context` | Biographical research | Era/role/tactical context for fair comparison |
| *(existing)* `shot-analysis` | The Numbers Game | Conversion rates, xG baselines |
| *(existing)* `possession-analysis` | The Numbers Game | Pass completion, turnover analysis |
| *(existing)* `pressing-game` | The Numbers Game | Regain rates, pressing metrics |
| *(existing)* `corner-analysis` | The Numbers Game | Set-piece conversion |

## Agents Created (in `.opencode/agents/`)

| Agent | Source | Role | Mode |
|---|---|---|---|
| `data-revolution` | Football Hackers (Biermann) | Explains data analytics in football — metrics, clubs, philosophy | primary |
| `tactical-context` | Inverting the Pyramid (Wilson) | Tactical history — formations, eras, rule changes | primary |
| `midfield-comparator` | Project-specific | Iniesta vs Zidane specialist — data pipeline, analysis, conclusions | primary |
| *(existing)* `data-scout` | The Numbers Game | Statistical player evaluation | primary |
| *(existing)* `football-accountant` | Charles Reep | Notation-based action tracking | primary |
| *(existing)* `match-analyst` | The Numbers Game | Opposition scouting and match analysis | primary |
| *(existing)* `tactical-analyst` | The Numbers Game | Formation, set-piece, pressing analysis | primary |

---

## The Six Analysis Pillars

| Pillar | Key Metrics |
|---|---|
| **Attack** | Goals, Assists, xG, xA, Shot-creating actions/90, Goal-creating actions/90 |
| **Possession** | Pass completion %, Progressive passes/90, Dribble success rate, Touches/90 |
| **Defense** | Pressures/90, Tackles/90, Interceptions/90, Blocks/90 |
| **Clutch** | Goals/assists in UCL KO, Finals, El Clásico/Derby, World Cup KO, Euros KO |
| **Consistency** | Seasons at elite level, Total minutes, Year-over-year variance, Peak duration |
| **Recognition** | Ballon d'Or wins/placements, UEFA POTY, FIFPro XI, League POTY awards |

No weights assigned — all dimensions presented neutrally as radar charts.

---

## Data Sources

| Source | Coverage | Status |
|---|---|---|
| FBref | Season + match data (both) | PENDING |
| Understat | xG/xA (Iniesta full, Zidane limited to ~1999+) | PENDING |
| Transfermarkt | Trophies, awards, market value | PENDING |
| StatsBomb (optional) | Event data for select matches | PENDING |

---

## Directory Structure

```
C:\Iniesta\
├── AGENTS.md                          ← this file
├── opencode.json
├── The Numbers Game.pdf
├── data/
│   ├── raw/                           ← scraped CSVs
│   ├── processed/                     ← cleaned/merged datasets
│   └── sources.md                     ← metadata on data sources
├── notebooks/
│   ├── 01-data-collection.ipynb
│   ├── 02-data-wrangling.ipynb
│   └── 03-analysis.ipynb
├── reports/
│   └── iniesta-vs-zidane.html
└── .opencode/
    ├── agents/
    │   ├── data-revolution.md
    │   ├── tactical-context.md
    │   ├── midfield-comparator.md
    │   └── ... (existing agents)
    └── skills/
        ├── statistical-modeling/
        ├── xg-model/
        ├── player-context/
        └── ... (existing skills)
```

---

## Next Steps (Phase 2)

When you're ready, continue the conversation and I will:
1. Create the `data/`, `notebooks/`, `reports/` directories
2. Write the data collection notebook (scrape FBref, Understat, Transfermarkt)
3. Start collecting match-by-match stats for both careers
4. Build the Iniesta-in-Barcelona-era and Zidane-in-Juve/Madrid-era datasets

---

## Known Challenges

| Challenge | Mitigation |
|---|---|
| Zidane pre-1999 data is sparse | Use season-level averages as fallback; mark confidence levels |
| Different positions (AM vs CM) | Compare by dimension (attack/defense separate) not raw totals |
| Different eras (tactics, rules) | Use player-context skill for every conclusion |
| Iniesta had stronger teammates | Note this but don't adjust — it's part of his career reality |
| Iniesta played more games (longer career) | Use per-90 metrics as primary comparison unit |
