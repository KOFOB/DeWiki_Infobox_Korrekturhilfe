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
        # Modify it with the values returned from the 'continue' section of the last result.
        req.update(last_continue)
        # Call API
        res = requests.get(URL, params=req).json()
        # I know just raising exception is not nice
        if 'error' in res:
            raise Exception(res['error'])
        if 'warnings' in res:
            print(res['warnings'])
        if 'query' in res:
            yield res['query']
        if 'continue' not in res:
            break
        last_continue = res['continue']


def extract_articles():
    f = open("articles.txt", "a")

    for result in query(PARAMS):
        pages = result["pages"]

        for k, v in pages.items():
            for links in v["links"]:
                f.write(links["title"])
                f.write('\n')

    f.close()
