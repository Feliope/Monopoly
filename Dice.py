import random
import tkinter as tk
from PIL import  ImageTk

class Dice:
    def __init__(self, game):
        self.game = game
        self.dice_image = ImageTk.PhotoImage(file=r"textures/dice.png")
        self.dice_1_image = ImageTk.PhotoImage(file=r"textures/dice-1.png")
        self.dice_2_image = ImageTk.PhotoImage(file=r"textures/dice-2.png")
        self.dice_3_image = ImageTk.PhotoImage(file=r"textures/dice-3.png")
        self.dice_4_image = ImageTk.PhotoImage(file=r"textures/dice-4.png")
        self.dice_5_image = ImageTk.PhotoImage(file=r"textures/dice-5.png")
        self.dice_6_image = ImageTk.PhotoImage(file=r"textures/dice-6.png")
        self.dice_1_display = None
        self.dice_2_display = None

    def roll(self):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        self.display(dice_1, dice_2)
        return dice_1, dice_2

    def display(self, dice_1, dice_2):
        dice_images = {
            1: self.dice_1_image,
            2: self.dice_2_image,
            3: self.dice_3_image,
            4: self.dice_4_image,
            5: self.dice_5_image,
            6: self.dice_6_image,
        }
        self.dice_1_display = tk.Label(self.game.screen, image=dice_images[dice_1], borderwidth=0, bg=self.game.BG_BOARD)
        self.dice_1_display.place(x=360, y=560, anchor="e")
        self.dice_2_display = tk.Label(self.game.screen, image=dice_images[dice_2], borderwidth=0, bg=self.game.BG_BOARD)
        self.dice_2_display.place(x=372, y=560, anchor="w")

    def destroy(self):
        if self.dice_1_display:
            self.dice_1_display.destroy()
        if self.dice_2_display:
            self.dice_2_display.destroy()
