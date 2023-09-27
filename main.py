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


def query(request):
    last_continue = {}
    while True:
        # Clone original request
        req = request.copy()
        # Modify it with the values returned in the 'continue' section of the last result.
        req.update(last_continue)
        # Call API
        result = requests.get(URL, params=req).json()

        # Removed error if-staement!!
        if 'warnings' in result:
            print(result['warnings'])
        if 'query' in result:
            yield result['query']
        if 'continue' not in result:
            break
        last_continue = result['continue']


for result in query(PARAMS):
    PAGES = result["pages"]

    for k, v in PAGES.items():
        for links in v["links"]:
            print(links["title"])