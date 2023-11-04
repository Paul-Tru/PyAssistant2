from bs4 import BeautifulSoup
import json
import requests
import config
from datetime import datetime
from colorama import Fore

# statements
fY = Fore.YELLOW
fR = Fore.RESET
fRed = Fore.RED

now = datetime.now()
date = now.strftime("%Y-%m-%d")
current = now.strftime("%H:%M")


# Tools
def change_bool(var, c_bool):
    config.var = c_bool
    with open('config.py', 'w') as f:
        f.write(f"{var} = {c_bool}")


def his(title):
    with open("log.json", "r") as file:
        try:
            log_data = json.load(file)
        except json.JSONDecodeError:
            log_data = {}

    new_entry = {"date": date}
    log_data[title] = new_entry

    with open("log.json", "w") as file:
        file.write(json.dumps(log_data, indent=4))



# Functions
def add_info(title, text):
    try:
        with open("info.json", "r") as file:
            try:
                info_data = json.load(file)
            except json.JSONDecodeError:
                info_data = {}

        new_entry = {"text": text, "date": date}
        info_data["info"][title] = new_entry

        with open("info.json", "w") as file:
            file.write(json.dumps(info_data, indent=4))
        his(title=title)
        return True

    except Exception as e:
        his(title=fRed + str(e) + fR)
        return e


def get_info(title):
    with open('info.json', 'r') as f:
        data = json.load(f)
    if title in data.get("info", {}):
        info_data = data["info"][title]
        text = info_data.get("text", "")
        date_get_info = info_data.get("date", "")
        return f"{text}\n\n{date_get_info}"
    else:
        return None


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
                his(title=title)
                return clean_html(article_text)
    else:
        return None

    return None


def clean_html(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup.get_text()


def ui():
    keyword(key_var=input())


def main():
    ui()


def keyword(key_var):
    if key_var.strip():
        print(key_var)
        get_wikipedia_var = get_wikipedia(title=key_var)
        get_info_var = get_info(title=key_var)
        if get_info_var is not None:
            print(get_info_var)
        elif get_wikipedia_var is not None:
            print(get_wikipedia_var)
        else:
            key_var = key_var + " not found"
            print("N/A")
        his(title=key_var)


if __name__ == "__main__":
    main()
