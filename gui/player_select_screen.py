import tkinter as tk
from PIL import ImageTk

def next_token(monopoly_instance, num):
    match num:
        case 1:
            monopoly_instance.player_1_index = (monopoly_instance.player_1_index + 1) % 10
            monopoly_instance.player_1_image = ImageTk.PhotoImage(
                file=monopoly_instance.display_tokens[monopoly_instance.player_1_index]
            )
            monopoly_instance.player_1_image_label.config(image=monopoly_instance.player_1_image)
        case 2:
            monopoly_instance.player_2_index = (monopoly_instance.player_2_index + 1) % 10
            monopoly_instance.player_2_image = ImageTk.PhotoImage(
                file=monopoly_instance.display_tokens[monopoly_instance.player_2_index]
            )
            monopoly_instance.player_2_image_label.config(image=monopoly_instance.player_2_image)
        case 3:
            monopoly_instance.player_3_index = (monopoly_instance.player_3_index + 1) % 10
            monopoly_instance.player_3_image = ImageTk.PhotoImage(
                file=monopoly_instance.display_tokens[monopoly_instance.player_3_index]
            )
            monopoly_instance.player_3_image_label.config(image=monopoly_instance.player_3_image)
        case 4:
            monopoly_instance.player_4_index = (monopoly_instance.player_4_index + 1) % 10
            monopoly_instance.player_4_image = ImageTk.PhotoImage(
                file=monopoly_instance.display_tokens[monopoly_instance.player_4_index]
            )
            monopoly_instance.player_4_image_label.config(image=monopoly_instance.player_4_image)

def prev_token(monopoly_instance, num):
    match num:
        case 1:
            monopoly_instance.player_1_index = (monopoly_instance.player_1_index + 9) % 10
            monopoly_instance.player_1_image = ImageTk.PhotoImage(
                file=monopoly_instance.display_tokens[monopoly_instance.player_1_index]
            )
            monopoly_instance.player_1_image_label.config(image=monopoly_instance.player_1_image)
        case 2:
            monopoly_instance.player_2_index = (monopoly_instance.player_2_index + 9) % 10
            monopoly_instance.player_2_image = ImageTk.PhotoImage(
                file=monopoly_instance.display_tokens[monopoly_instance.player_2_index]
            )
            monopoly_instance.player_2_image_label.config(image=monopoly_instance.player_2_image)
        case 3:
            monopoly_instance.player_3_index = (monopoly_instance.player_3_index + 9) % 10
            monopoly_instance.player_3_image = ImageTk.PhotoImage(
                file=monopoly_instance.display_tokens[monopoly_instance.player_3_index]
            )
            monopoly_instance.player_3_image_label.config(image=monopoly_instance.player_3_image)
        case 4:
            monopoly_instance.player_4_index = (monopoly_instance.player_4_index + 9) % 10
            monopoly_instance.player_4_image = ImageTk.PhotoImage(
                file=monopoly_instance.display_tokens[monopoly_instance.player_4_index]
            )
            monopoly_instance.player_4_image_label.config(image=monopoly_instance.player_4_image)

def change_type(monopoly_instance, player, num):
    player.change_type()  
    button = getattr(monopoly_instance, f"player_{num}_type_button")
    button.config(text=f"{player.type.upper()}")

def player_select_screen(monopoly_instance):
    monopoly_instance.title_screen.destroy()

    monopoly_instance.select_screen = tk.Frame(monopoly_instance.root, bg=monopoly_instance.BG_DARK)
    monopoly_instance.select_screen.pack(fill="both", expand=True)

    right_image = ImageTk.PhotoImage(file=r"textures\right-arrow.png")
    left_image = ImageTk.PhotoImage(file=r"textures\left-arrow.png")
    type_button_image = ImageTk.PhotoImage(file=r"textures\type-button.png")

    title = tk.Label(
        monopoly_instance.select_screen, image=monopoly_instance.title_image, borderwidth=0, bg=monopoly_instance.BG_DARK
    )
    title.place(relx=0.5, y=50, anchor="n")
    player_select = tk.Label(
        monopoly_instance.select_screen,
        borderwidth=0,
        font=monopoly_instance.BIG_FONT,
        text="Informe os jogadores",
        bg=monopoly_instance.BG_DARK,
        fg="white",
    )
    player_select.place(x=435, y=162.5, width=400, height=53, anchor="nw")
    start_button = tk.Button(
        monopoly_instance.select_screen,
        borderwidth=0,
        text="INICIAR",
        font=monopoly_instance.FONT,
        compound="center",
        image=monopoly_instance.button_image,
        bg=monopoly_instance.BG_DARK,
        activebackground=monopoly_instance.BG_DARK,
        command=monopoly_instance.start_game,
    )
    start_button.place(relx=0.5, y=670, width=170, height=62, anchor="s")

    monopoly_instance.player_1_index = 0
    monopoly_instance.player_1_image = ImageTk.PhotoImage(file=monopoly_instance.display_tokens[0])
    monopoly_instance.player_1_image_label = tk.Label(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=monopoly_instance.player_1_image,
        bg=monopoly_instance.BG_DARK,
    )
    monopoly_instance.player_1_image_label.place(x=188, y=393.5, anchor="nw")
    monopoly_instance.player_1_entry = tk.Entry(
        monopoly_instance.select_screen,
        borderwidth=0,
        font=monopoly_instance.FONT,
        justify="center",
        fg="grey",
    )
    monopoly_instance.player_1_entry.place(x=252, y=303.5, width=144, height=45, anchor="center")
    monopoly_instance.player_1_entry.insert(0, "Jogador 1")
    monopoly_instance.player_1_entry.bind(
        "<FocusIn>",
        lambda _: (
            monopoly_instance.player_1_entry.delete(0, tk.END),
            monopoly_instance.player_1_entry.configure(fg="black"),
        )
        if monopoly_instance.player_1_entry.get() == "Jogador 1"
        else None,
    )
    monopoly_instance.player_1_entry.bind(
        "<FocusOut>",
        lambda _: (
            monopoly_instance.player_1_entry.insert(0, "Jogador 1"),
            monopoly_instance.player_1_entry.configure(fg="grey"),
        )
        if monopoly_instance.player_1_entry.get() == ""
        else None,
    )
    monopoly_instance.player_1_type_button = tk.Button(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=type_button_image,
        text="HUMANO",
        compound="center",
        font=monopoly_instance.SMALL_FONT,
        bg=monopoly_instance.BG_DARK,
        activebackground=monopoly_instance.BG_DARK,
        command=lambda: change_type(monopoly_instance, monopoly_instance.player_1, 1),
    )
    monopoly_instance.player_1_type_button.place(x=252, y=393.5, anchor="s")
    player_1_left = tk.Button(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=left_image,
        bg=monopoly_instance.BG_DARK,
        activebackground=monopoly_instance.BG_DARK,
        command=lambda: prev_token(monopoly_instance, 1),
    )
    player_1_left.place(x=140, y=441.5, anchor="nw")
    player_1_right = tk.Button(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=right_image,
        bg=monopoly_instance.BG_DARK,
        activebackground=monopoly_instance.BG_DARK,
        command=lambda: next_token(monopoly_instance, 1),
    )
    player_1_right.place(x=332, y=441.5, anchor="nw")

    monopoly_instance.player_2_index = 1
    monopoly_instance.player_2_image = ImageTk.PhotoImage(file=monopoly_instance.display_tokens[1])
    monopoly_instance.player_2_image_label = tk.Label(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=monopoly_instance.player_2_image,
        bg=monopoly_instance.BG_DARK,
    )
    monopoly_instance.player_2_image_label.place(x=444, y=393.5, anchor="nw")
    monopoly_instance.player_2_entry = tk.Entry(
        monopoly_instance.select_screen,
        borderwidth=0,
        font=monopoly_instance.FONT,
        justify="center",
        fg="grey",
    )
    monopoly_instance.player_2_entry.place(x=508, y=303.5, width=144, height=45, anchor="center")
    monopoly_instance.player_2_entry.insert(0, "Jogador 2")
    monopoly_instance.player_2_entry.bind(
        "<FocusIn>",
        lambda _: (
            monopoly_instance.player_2_entry.delete(0, tk.END),
            monopoly_instance.player_2_entry.configure(fg="black"),
        )
        if monopoly_instance.player_2_entry.get() == "Jogador 2"
        else None,
    )
    monopoly_instance.player_2_entry.bind(
        "<FocusOut>",
        lambda _: (
            monopoly_instance.player_2_entry.insert(0, "Jogador 2"),
            monopoly_instance.player_2_entry.configure(fg="grey"),
        )
        if monopoly_instance.player_2_entry.get() == ""
        else None,
    )
    monopoly_instance.player_2_type_button = tk.Button(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=type_button_image,
        text="NPC",
        compound="center",
        font=monopoly_instance.SMALL_FONT,
        bg=monopoly_instance.BG_DARK,
        activebackground=monopoly_instance.BG_DARK,
        command=lambda: change_type(monopoly_instance, monopoly_instance.player_2, 2),
    )
    monopoly_instance.player_2_type_button.place(x=508, y=393.5, anchor="s")
    player_2_left = tk.Button(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=left_image,
        bg=monopoly_instance.BG_DARK,
        activebackground=monopoly_instance.BG_DARK,
        command=lambda: prev_token(monopoly_instance, 2),
    )
    player_2_left.place(x=396, y=441.5, anchor="nw")
    player_2_right = tk.Button(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=right_image,
        bg=monopoly_instance.BG_DARK,
        activebackground=monopoly_instance.BG_DARK,
        command=lambda: next_token(monopoly_instance, 2),
    )
    player_2_right.place(x=588, y=441.5, anchor="nw")

    monopoly_instance.player_3_index = 2
    monopoly_instance.player_3_image = ImageTk.PhotoImage(file=monopoly_instance.display_tokens[2])
    monopoly_instance.player_3_image_label = tk.Label(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=monopoly_instance.player_3_image,
        bg=monopoly_instance.BG_DARK,
    )
    monopoly_instance.player_3_image_label.place(x=708, y=393.5, anchor="nw")
    monopoly_instance.player_3_entry = tk.Entry(
        monopoly_instance.select_screen,
        borderwidth=0,
        font=monopoly_instance.FONT,
        justify="center",
        fg="grey",
    )
    monopoly_instance.player_3_entry.place(x=772, y=303.5, width=144, height=45, anchor="center")
    monopoly_instance.player_3_entry.insert(0, "Jogador 3")
    monopoly_instance.player_3_entry.bind(
        "<FocusIn>",
        lambda _: (
            monopoly_instance.player_3_entry.delete(0, tk.END),
            monopoly_instance.player_3_entry.configure(fg="black"),
        )
        if monopoly_instance.player_3_entry.get() == "Jogador 3"
        else None,
    )
    monopoly_instance.player_3_entry.bind(
        "<FocusOut>",
        lambda _: (
            monopoly_instance.player_3_entry.insert(0, "Jogador 3"),
            monopoly_instance.player_3_entry.configure(fg="grey"),
        )
        if monopoly_instance.player_3_entry.get() == ""
        else None,
    )
    monopoly_instance.player_3_type_button = tk.Button(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=type_button_image,
        text="NPC",
        compound="center",
        font=monopoly_instance.SMALL_FONT,
        bg=monopoly_instance.BG_DARK,
        activebackground=monopoly_instance.BG_DARK,
        command=lambda: change_type(monopoly_instance, monopoly_instance.player_3, 3),
    )
    monopoly_instance.player_3_type_button.place(x=772, y=393.5, anchor="s")
    player_3_left = tk.Button(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=left_image,
        bg=monopoly_instance.BG_DARK,
        activebackground=monopoly_instance.BG_DARK,
        command=lambda: prev_token(monopoly_instance, 3),
    )
    player_3_left.place(x=660, y=441.5, anchor="nw")
    player_3_right = tk.Button(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=right_image,
        bg=monopoly_instance.BG_DARK,
        activebackground=monopoly_instance.BG_DARK,
        command=lambda: next_token(monopoly_instance, 3),
    )
    player_3_right.place(x=852, y=441.5, anchor="nw")

    monopoly_instance.player_4_index = 3
    monopoly_instance.player_4_image = ImageTk.PhotoImage(file=monopoly_instance.display_tokens[3])
    monopoly_instance.player_4_image_label = tk.Label(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=monopoly_instance.player_4_image,
        bg=monopoly_instance.BG_DARK,
    )
    monopoly_instance.player_4_image_label.place(x=964, y=393.5, anchor="nw")
    monopoly_instance.player_4_entry = tk.Entry(
        monopoly_instance.select_screen,
        borderwidth=0,
        font=monopoly_instance.FONT,
        justify="center",
        fg="grey",
    )
    monopoly_instance.player_4_entry.place(
        x=1028, y=303.5, width=144, height=45, anchor="center"
    )
    monopoly_instance.player_4_entry.insert(0, "Jogador 4")
    monopoly_instance.player_4_entry.bind(
        "<FocusIn>",
        lambda _: (
            monopoly_instance.player_4_entry.delete(0, tk.END),
            monopoly_instance.player_4_entry.configure(fg="black"),
        )
        if monopoly_instance.player_4_entry.get() == "Jogador 4"
        else None,
    )
    monopoly_instance.player_4_entry.bind(
        "<FocusOut>",
        lambda _: (
            monopoly_instance.player_4_entry.insert(0, "Jogador 4"),
            monopoly_instance.player_4_entry.configure(fg="grey"),
        )
        if monopoly_instance.player_4_entry.get() == ""
        else None,
    )
    monopoly_instance.player_4_type_button = tk.Button(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=type_button_image,
        text="NPC",
        compound="center",
        font=monopoly_instance.SMALL_FONT,
        bg=monopoly_instance.BG_DARK,
        activebackground=monopoly_instance.BG_DARK,
        command=lambda: change_type(monopoly_instance, monopoly_instance.player_4, 4),
    )
    monopoly_instance.player_4_type_button.place(x=1028, y=393.5, anchor="s")
    player_4_left = tk.Button(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=left_image,
        bg=monopoly_instance.BG_DARK,
        activebackground=monopoly_instance.BG_DARK,
        command=lambda: prev_token(monopoly_instance, 4),
    )
    player_4_left.place(x=916, y=441.5, anchor="nw")
    player_4_right = tk.Button(
        monopoly_instance.select_screen,
        borderwidth=0,
        image=right_image,
        bg=monopoly_instance.BG_DARK,
        activebackground=monopoly_instance.BG_DARK,
        command=lambda: next_token(monopoly_instance, 4),
    )
    player_4_right.place(x=1108, y=441.5, anchor="nw")

    monopoly_instance.root.mainloop()
