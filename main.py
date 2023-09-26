import requests

S = requests.Session()

URL = "https://de.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "Benutzer:Aka/Fehlerlisten/Handgestrickte Infoboxen",
    "prop": "links",
    "pllimit": "500"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    for l in v["links"]:
        print(l["title"])