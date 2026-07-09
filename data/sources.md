# Data Sources: Iniesta vs Zidane

## Primary Sources Collected

### Wikipedia (successfully scraped)
- **URLs**: 
  - https://en.wikipedia.org/wiki/Andr%C3%A9s_Iniesta
  - https://en.wikipedia.org/wiki/Zinedine_Zidane
- **Data**: Club career tables (goals, appearances by season/competition), international career tables
- **Files**: `iniesta_wiki_club.csv`, `iniesta_wiki_intl.csv`, `zidane_wiki_club.csv`, `zidane_wiki_intl.csv`
- **Limitations**: Only basic stats (apps, goals); no xG, passing %, or defensive actions

### Manual Compilation (known career data)
- **Data**: Career summary metrics, trophy/award lists from verified public records
- **Files**: `career_summary.csv`, `iniesta_honours.csv`, `zidane_honours.csv`
- **Sources consulted**: Transfermarkt, UEFA, FIFA, league records

---

## Sources Attempted (blocked by Cloudflare)

| Source | Status | Reason |
|---|---|---|
| FBref | ❌ Blocked | Cloudflare JS challenge — all automated approaches failed (requests, cloudscraper, selenium, undetected-chromedriver) |
| Transfermarkt | ❌ Blocked | JS-rendered content — static requests return no data tables |
| Understat | ❌ No data | Iniesta peak predates 2014/15 coverage; Zidane retired 2006 |

### FBref URLs (for manual CSV download from browser)
- Iniesta: https://fbref.com/en/players/cfd65a29/Andres-Iniesta
- Zidane: https://fbref.com/en/players/654f4e63/Zinedine-Zidane

To manually download: open URL in browser → scroll to table → click "CSV" button → save to `data/raw/`

---

## Recommended Next Steps for Phase 3 (Data Wrangling)

1. Merge Wikipedia club + intl tables into unified player-season datasets
2. Calculate per-90 metrics from the app/minutes data
3. If FBref CSV exported manually, merge xG/xA, passing, and defensive stats
4. Structure data for the six analysis pillars: Attack, Possession, Defense, Clutch, Consistency, Recognition
