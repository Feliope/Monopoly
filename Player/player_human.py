from Player.player import Player
import tkinter as tk

class PlayerHuman(Player):
    def __init__(self, name):
        super().__init__(name, player_type="human")

    def take_turn(self, game):
        dice_button = tk.Button(
            game.screen,
            image=game.dice_image,
            borderwidth=0,
            bg=game.BG_BUTTON,
            activebackground=game.BG_BUTTON,
            command=lambda: (game.end_turn_display(), game.player_turn(), dice_button.destroy())
        )
        dice_button.place(x=1032, y=532, anchor="nw")
