import requests
import json


r = requests.get('https://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json')
events = r.json()
hero_name = events['data']

search_key = input("input nama hero")
hero = [x for key, x in hero_name.items() if search_key in key]

# syntax print
#json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
output = json.dumps(hero,indent = 2, separators =(", ", " : "))
print(output)
