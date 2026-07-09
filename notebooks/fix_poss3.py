import json

with open('notebooks/02-data-wrangling.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        src = ''.join(cell['source'])
        if 'build_possession_pillar' in src:
            lines = cell['source']
            new_lines = []
            for line in lines:
                if line.strip().startswith('poss = iniesta_sb_liga[['):
                    new_lines.append('    # Use passes + minutes_est to compute passes_per_90, not the raw column\n')
                elif line.strip().startswith('                            "passes_per90", "dribbles", "minutes_est"'):
                    new_lines.append('                            "passes", "dribbles", "minutes_est",\n')
                elif '"pass_completion_pct"' in line and 'round' in line:
                    new_lines.append('    poss["pass_completion_pct"] = poss["pass_completion_pct"].round(1)\n')
                    new_lines.append('    poss["passes_per_90"] = (poss["passes"] / poss["minutes_est"] * 90).round(1)\n')
                else:
                    new_lines.append(line)
            cell['source'] = new_lines
            print(f'Fixed possession pillar cell {i}')
            break

with open('notebooks/02-data-wrangling.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print('Saved')
