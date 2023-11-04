import GUI
import tools as t


def ui():
    t.keyword(key_var=input())


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


if __name__ == "__main__":
    main()
