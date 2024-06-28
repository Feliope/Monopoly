import itertools
import csv
from Property import Property
import tkinter as tk
from PIL import ImageTk

class Board:
    def __init__(self, game):
        self.game = game
        self.board_image = ImageTk.PhotoImage(file=r"textures/board.png")
        self.board = tk.Canvas(self.game.screen, borderwidth=0, highlightthickness=0)
        self.board.place(width=720, height=717, anchor="nw")
        self.board.create_image(0, 0, image=self.board_image, anchor="nw")
        self.property_locations = self.load_properties()

    def load_properties(self):
        property_locations = {}
        property_locations_list = itertools.cycle(range(1, 41))
        with open("properties.csv", "r", newline="") as file:
            for property_info in csv.reader(file):
                property_instance = Property(property_info[0], int(property_info[1]), property_info[2], eval(property_info[3]))
                property_locations[next(property_locations_list)] = property_instance
        return property_locations

    def move_player(self, player, x, y):
        self.board.coords(player.token, x, y)
