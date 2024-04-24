import requests
import json


r = requests.get('https://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json')
events = r.json()
hero_name = events['data']

search_key = input("input nama hero")
hero = [x for key, x in hero_name.items() if search_key in key]

output = json.dumps(hero,indent = 2, separators =(", ", " : "))
print(output)
