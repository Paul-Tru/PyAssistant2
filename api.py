import tools as t
import json
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
    lan = t.config_var("moviedb", "lan")
    print(lan)
    choice = choice.lower()
    print(choice)
    keyword = keyword.replace(" ", "%20")
    if keyword == "actor":
        keyword = "person"
    print(keyword)
    url = f"https://api.themoviedb.org/3/search/{choice}?query={keyword}&include_adult=false&language={lan}&page=1"
    print(url)
    auth = frozenset(t.auth("AUTH"))
    print(auth)
    headers = {
        "accept": "application/json",
        "Authorization": auth
    }
    print(headers)

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    print(data)

get_moviedb("movie", "snowden")
