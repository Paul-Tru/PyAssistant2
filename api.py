import tools as t
import requests


def get_wikipedia(title):
    base_url = "https://de.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "titles": title
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    if "query" in data:
        pages = data["query"]["pages"]
        for page_id, page_info in pages.items():
            if page_id != "-1":
                article_text = page_info["extract"]
                t.his(title=title)
                return t.clean_html(article_text)
    else:
        return None

    return None


def get_moviedb(choice, keyword):
    lan = t.config_var(sec="moviedb", var="lan")
    choice = choice.lower()
    keyword = keyword.replace(" ", "%20")
    if keyword == "actor":
        keyword = "person"
    url = f"https://api.themoviedb.org/3/search/{choice}?query={keyword}&include_adult=false&language={lan}&page=1"
    auth = frozenset(t.auth(var="AUTH"))
    headers = {
        "accept": "application/json",
        "Authorization": auth
    }

    response = requests.get(url, headers=headers)

    print(response.text)
