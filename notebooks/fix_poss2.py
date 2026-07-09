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
                # Keep the assignment line
                if line.strip().startswith("poss[\"passes_per_90\"] = poss[\"passes_per90\"]"):
                    new_lines.append(line)
                elif line.strip() == '\"passes_per_90\": \"N/A (pre-analytics era)\",' and 'player' not in line:
                    # Skip duplicate - keep only one occurrence
                    pass
                else:
                    new_lines.append(line)
            # Add the round line at the right place
            final = []
            added_round = False
            for line in new_lines:
                if 'poss[\"pass_completion_pct\"]' in line and not added_round:
                    final.append(line)
                    final.append('    poss["passes_per_90"] = poss["passes_per90"].round(1)\n')
                    added_round = True
                else:
                    final.append(line)
            cell['source'] = final
            print(f'Fixed possession pillar cell {i}')
            break

with open('notebooks/02-data-wrangling.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print('Saved')
