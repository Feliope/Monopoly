import tkinter as tk
from PIL import ImageTk
from gui.player_select_screen import player_select_screen

def title_screen_display(monopoly_instance):
    monopoly_instance.clear_screen()

    monopoly_instance.title_screen = tk.Frame(monopoly_instance.root, bg=monopoly_instance.BG_DARK)
    monopoly_instance.title_screen.pack(fill="both", expand=True)

    monopoly_instance.button_image = ImageTk.PhotoImage(file=r"textures/button.png")
    monopoly_instance.new_button = ImageTk.PhotoImage(file=r"textures/new.png")

    title = tk.Label(
        monopoly_instance.title_screen, image=monopoly_instance.title_image, borderwidth=0, bg=monopoly_instance.BG_DARK
    )
    title.place(relx=0.5, y=50, anchor="n")

    offline_button = tk.Button(
        monopoly_instance.title_screen,
        borderwidth=0,
        text="Novo Jogo",
        font=monopoly_instance.SMALL_FONT,
        compound="center",
        image=monopoly_instance.new_button,
        bg=monopoly_instance.BG_DARK,
        activebackground=monopoly_instance.BG_DARK,
        command=lambda: player_select_screen(monopoly_instance),
    )
    offline_button.place(x=570, y=250, anchor="nw")

    monopoly_instance.root.mainloop()
