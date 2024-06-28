from Player.player import Player
import random
import tkinter as tk

class PlayerIA(Player):
    def __init__(self, name):
        super().__init__(name, player_type="npc")

    def make_decision(self, game):
        if self.money > 200:
            available_properties = [
                prop for prop in game.property_locations.values() 
                if prop["owned_by"] is None and prop["price"] <= self.money
            ]
            if available_properties:
                chosen_property = random.choice(available_properties)
                self.buy_property(chosen_property)
                game.update_game_state_after_purchase(chosen_property, self)

    def buy_property(self, property):
        self.update_money(-property["price"])
        self.add_property(property)
        property["owned_by"] = self

    def take_turn(self, game):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        roll_no = dice_1 + dice_2

        game.dice_display(dice_1, dice_2)

        if self.location + roll_no > 40:
            roll_difference = 40 - (self.location + roll_no)
            self.update_location(-roll_difference)
            salary_display = tk.Label(
                game.screen,
                text=f"{self.name} Recebeu $200 de salário",
                borderwidth=0,
                bg=game.BG_BOARD,
                font=game.SMALL_FONT,
            )
            salary_display.place(x=360, y=300, anchor="n")
            self.update_money(200)
            game.update_money()
        else:
            self.update_location(self.location + roll_no)

        game.current_player_location_property = game.property_locations[self.location]

        x, y = game.current_player_location_property["coords"]
        game.board.coords(self.token, x, y)
        current_player_landing_text = f"{self.name} Tirou {roll_no}\n&\nChegou em {game.current_player_location_property['name']}"
        game.current_player_landing = tk.Label(game.screen, text=current_player_landing_text, bg=game.BG_BOARD, borderwidth=0, font=game.SMALL_FONT)
        game.current_player_landing.place(x=360, y=145, anchor="n")

        game.notify_observers({"event": "player_move", "player_name": self.name, "property_name": game.current_player_location_property["name"]})

        if game.current_player_location_property["colour"] not in [
            "Go",
            "Community Chest",
            "Chance",
            "Tax",
            "Jail",
            "Go to Jail",
            "Free Parking",
        ]:
            if game.current_player_location_property["owned_by"] not in [game.player_1, game.player_2, game.player_3, game.player_4]:
                if game.current_player_location_property["price"] <= self.money:
                    if random.randint(0, 4):
                        game.root.after(500, lambda: (self.buy_property(game.current_player_location_property), game.update_game_state_after_purchase(game.current_player_location_property, self)))

            elif game.current_player_location_property["colour"] == "Utility":
                if self != game.current_player_location_property["owned_by"]:
                    game.pay_utility()
            else:
                if self != game.current_player_location_property["owned_by"]:
                    game.pay_rent()
        elif game.current_player_location_property["colour"] == "Tax":
            game.pay_tax()
        elif game.current_player_location_property["colour"] in ["Chance", "Community Chest"]:
            game.show_card()
        elif game.current_player_location_property["colour"] == "Go to Jail":
            self.update_location(11)
            action_display = tk.Label(
                game.screen, text=f"{self.name} foi para a prisão", borderwidth=0, bg=game.BG_BOARD, font=game.SMALL_FONT
            )
            action_display.place(x=360, y=260, anchor="n")
            game.board.coords(self.token, 63, 660)
            game.root.after(500, game.pay_fine)

        game.root.after(1500, game.end_turn_func)
