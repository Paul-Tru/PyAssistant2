import customtkinter
import keyboard
import main


def open_window():

    # commands
    def on_enter(event):
        keyword = entry.get()
        main.his(title=keyword)
        main.keyword(key_var=keyword)
        entry.delete(0, 'end')

    # design
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("dark-blue")

    # size
    root = customtkinter.CTk()
    root.geometry("300x250")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    # title
    label = customtkinter.CTkLabel(master=frame, text="PyAssistant", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    # input
    entry = customtkinter.CTkEntry(master=frame, placeholder_text="Keyword")
    entry.pack(pady=12, padx=10)

    entry.bind('<Return>', on_enter)

    # buttons
    button = customtkinter.CTkButton(master=frame, text="Quit", command=root.destroy)
    button.pack(pady=12, padx=10)
    root.mainloop()


keyboard.add_hotkey('f10', open_window)
keyboard.wait()
