import customtkinter as ctk
import configparser
import keyboard
import tools as t

# design
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")


def open_window():
    # commands
    def on_enter(event):
        keyword = entry.get()
        if keyword.strip():
            t.his(title=keyword)
            t.keyword(key_var=keyword)
            entry.delete(0, 'end')

    # size
    root = ctk.CTk()
    root.geometry("300x250")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    # title
    label = ctk.CTkLabel(master=frame, text="PyAssistant", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    # input
    entry = ctk.CTkEntry(master=frame, placeholder_text="Keyword")
    entry.pack(pady=12, padx=10)

    entry.bind('<Return>', on_enter)

    # buttons
    button = ctk.CTkButton(master=frame, text="Quit", command=root.destroy)
    button.pack(pady=12, padx=10)
    root.mainloop()


def change_bool_status():
    filename = "config.ini"

    def toggle_variable(filename, section, variable, button):
        config = configparser.ConfigParser()
        config.read(filename)
        current_value = config.getboolean(section, variable)
        config.set(section, variable, str(not current_value))
        with open(filename, 'w') as configfile:
            config.write(configfile)
        if not current_value:
            button.configure(fg_color='green')
        else:
            button.configure(fg_color='red')

    def create_button(root, filename, section, variable):
        button = ctk.CTkButton(master=root, text=f"{variable}")
        config = configparser.ConfigParser()
        config.read(filename)
        if config.getboolean(section, variable):
            button.configure(fg_color='green', font=("Roboto", 12))
        else:
            button.configure(fg_color='red', font=("Roboto", 12))

        button.configure(command=lambda s=section, v=variable, b=button: toggle_variable(filename, s, v, b))

        return button

    def create_window():
        root = ctk.CTk()
        config = configparser.ConfigParser()
        config.read("config.ini")

        for section in config.sections():
            frame = ctk.CTkFrame(master=root)
            frame.pack(pady=5, padx=5)

            label = ctk.CTkLabel(master=frame, text=f"{section}", font=("Roboto", 15))
            label.pack(pady=5, padx=5)

            for variable in config[section]:
                button = create_button(frame, filename, section, variable)
                button.pack(pady=5, padx=5)


        save_button = ctk.CTkButton(master=root, text="Save", command=root.destroy, font=("Roboto", 12))
        save_button.pack(pady=5, padx=5)

        root.mainloop()

    create_window()

keyboard.add_hotkey('f10', open_window)
keyboard.wait()


def available():
    return True

