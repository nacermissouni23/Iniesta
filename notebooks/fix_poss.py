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
                # Remove duplicate passes_per90 assignment
                if line.strip().startswith("poss[\"passes_per_90\"] = poss[\"passes_per90\"]"):
                    continue
                new_lines.append(line)
            cell['source'] = new_lines

            # Now fix the Zidane row to remove duplicate key
            src2 = ''.join(cell['source'])
            # Find and fix: two passes_per_90 keys in the Zidane dict
            old = '"passes_per_90": "N/A (pre-analytics era)",\n        "passes_per_90": "N/A (pre-analytics era)",'
            new = '"passes_per_90": "N/A (pre-analytics era)",'
            if old in src2:
                src2 = src2.replace(old, new)
                cell['source'] = src2.splitlines(True)
                # The last line won't have proper newline... fix
                if cell['source'] and not cell['source'][-1].endswith('\n'):
                    cell['source'][-1] = cell['source'][-1] + '\n'

            print(f'Fixed possession pillar cell {i}')
            break

with open('notebooks/02-data-wrangling.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print('Saved')
