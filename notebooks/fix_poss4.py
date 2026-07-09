import json

with open('notebooks/02-data-wrangling.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        src = ''.join(cell['source'])
        if 'build_possession_pillar' in src:
            # Replace the entire cell source
            cell['source'] = [
                'def build_possession_pillar(iniesta_sb_liga):\n',
                '    if len(iniesta_sb_liga) == 0:\n',
                '        return pd.DataFrame()\n',
                '\n',
                '    poss = iniesta_sb_liga[["season", "season_start", "matches",\n',
                '                            "passes", "pass_completed", "pass_completion_pct",\n',
                '                            "dribbles", "minutes_est"]].copy()\n',
                '    poss["player"] = "Andres Iniesta"\n',
                '    poss["pass_completion_pct"] = poss["pass_completion_pct"].round(1)\n',
                '    poss["passes_per_90"] = (poss["passes"] / poss["minutes_est"] * 90).round(1)\n',
                '\n',
                '    # Zidane row with note\n',
                '    zidane_row = pd.DataFrame([{\n',
                '        "player": "Zinedine Zidane",\n',
                '        "season": "N/A",\n',
                '        "season_start": np.nan,\n',
                '        "matches": np.nan,\n',
                '        "passes": np.nan,\n',
                '        "pass_completed": np.nan,\n',
                '        "pass_completion_pct": "~82% (estimated from historical accounts)",\n',
                '        "passes_per_90": "N/A (pre-analytics era)",\n',
                '        "dribbles": np.nan,\n',
                '        "minutes_est": np.nan,\n',
                '    }])\n',
                '\n',
                '    return pd.concat([poss, zidane_row], ignore_index=True)\n',
                '\n',
                '\n',
                'possession_pillar = build_possession_pillar(iniesta_sb_liga)\n',
                'print(f"possession_pillar: {possession_pillar.shape[0]} rows, {possession_pillar.shape[1]} cols")\n',
                'display(possession_pillar)\n',
            ]
            print(f'Rewrote possession pillar cell {i}')
            break

with open('notebooks/02-data-wrangling.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print('Saved')
