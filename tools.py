from bs4 import BeautifulSoup
import json
from datetime import datetime
from colorama import Fore
import configparser
import os
from dotenv import load_dotenv

import GUI
import api

# statements
fY = Fore.YELLOW
fR = Fore.RESET
fRed = Fore.RED


now = datetime.now()
date = now.strftime("%Y-%m-%d")
current = now.strftime("%H:%M")


def keyword(key_var):
    print(key_var)
    if key_var.startswith("/"):
        commands(key_var)
    else:
        get_wikipedia_var = api.get_wikipedia(key_var)
        get_info_var = get_info(key_var)
        if get_info_var is not None:
            print(get_info_var)
        elif get_wikipedia_var is not None:
            print(get_wikipedia_var)
            GUI.answer(key_var, get_wikipedia_var)
        else:
            print("N/A")
        his(key_var)


def commands(key_var):
    key_var = key_var.replace("/", "")
    if key_var == "bool":
        GUI.change_bool_status()
    elif key_var == "tts":
        change_bool("functions", "tts_var")
    elif key_var == "moviedb":
        c, k = GUI.moviedb()
        api.get_moviedb(c, k)
    elif key_var.startswith("add"):
        key_var = key_var.replace("add", "")
        parts = key_var.split("; ")
        ti, te = parts[0], parts[1]
        add_info(ti, te)


def change_bool(sec, var):
    config = configparser.ConfigParser()
    config.read("config.ini")
    if config.has_option(sec, var):
        current_value = config.getboolean(sec, var)
        config.set(sec, var, str(not current_value))
        with open("config.ini", 'w') as configfile:
            config.write(configfile)
    else:
        print(f"Option {var} not found in section {sec}")


def config_var(sec, var):
    config = configparser.ConfigParser()
    config.read("config_var.ini")
    val = config.get(sec, var)
    return val


def auth(var):
    print(var)
    load_dotenv()
    return os.getenv(var)


def get_variable(sec, var):
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config.get(sec, var)


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


def clean_html(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup.get_text()


def available():
    return True
