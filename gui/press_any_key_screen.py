from gui.title_screen import title_screen_display

import tkinter as tk
from PIL import ImageTk

def menu_screen_display(monopoly_instance):
    for widget in monopoly_instance.root.winfo_children():
        widget.destroy()

    background_image = ImageTk.PhotoImage(file=r"textures/background.jpg")
    dark_bg = ImageTk.PhotoImage(file=r"textures/dark-bg.jpg")
    exit_bg = ImageTk.PhotoImage(file=r"textures/exit-bg.jpg")

    menu_screen = tk.Canvas(monopoly_instance.root, borderwidth=0)
    menu_screen.pack(fill="both", expand=True)

    menu_screen.create_image(0, 0, image=background_image, anchor="nw")
    menu_screen.create_image(640, 50, image=monopoly_instance.title_image, anchor="n")
    transparent_label = tk.Label(
        menu_screen,
        borderwidth=0,
        image=dark_bg,
        text="Aperte qualquer tecla para continuar...",
        font=monopoly_instance.BIG_FONT,
        fg="white",
        compound="center",
    )
    transparent_label.place(height=50, width=1276, relx=0.5, rely=0.75, anchor="n")
    exit_button = tk.Button(
        menu_screen,
        borderwidth=0,
        image=exit_bg,
        command=monopoly_instance.root.destroy,
        activebackground="#4AD9FF",
    )
    exit_button.place(height=48, width=48, x=1278, y=2, anchor="ne")

    menu_screen.bind("<KeyPress>", lambda _: title_screen_display(monopoly_instance))

    menu_screen.focus_set()

    monopoly_instance.root.mainloop()
