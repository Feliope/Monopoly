from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, player_type="human"):
        self.name = name
        self.location = 1
        self.money = 1500
        self.properties = []
        self.turn = False
        self.type = player_type

    def update_location(self, new_location):
        self.location = new_location

    def update_money(self, amount):
        self.money += amount

    def add_property(self, property):
        self.properties.append(property)

    def set_turn(self, turn):
        self.turn = turn

    def change_type(self):
        self.type = "npc" if self.type == "human" else "human"

    def has_property(self, property):
        return property in self.properties

    @abstractmethod
    def take_turn(self, game):
        pass
