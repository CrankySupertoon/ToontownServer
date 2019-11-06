import json

with open('settings/game_settings.json', 'r') as loop:
            data = json.load(loop)

print(data["Login Settings"]["IP Address"])