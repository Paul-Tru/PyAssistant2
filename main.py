import GUI
import tools as t


def ui():
    keyword(key_var=input())


def main():
    ui()


def status():
    s_g = False
    s_t = False
    if GUI.available():
        s_g = True
    if t.available():
        s_t = True
    return s_g, s_t


def keyword(key_var):
    print(key_var)
    get_wikipedia_var = t.get_wikipedia(title=key_var)
    get_info_var = t.get_info(title=key_var)
    if get_info_var is not None:
        print(get_info_var)
    elif get_wikipedia_var is not None:
        print(get_wikipedia_var)
    else:
        print("N/A")
    t.his(title=key_var)


if __name__ == "__main__":
    main()
