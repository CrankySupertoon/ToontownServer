import json

with open('settings/controls.json') as loop:
        data = json.load(loop)

print(data["Controls"][0]['walk-up'])