import csv
import random
import tkinter as tk

class Cards:
    def __init__(self, game):
        self.chance_list = []
        self.chest_list = []
        self.game = game
        self.load_cards()

    def load_cards(self):
        self.chance_list.clear()
        self.chest_list.clear()
        with open("cards.csv", "r", newline="") as file:
            for card_info in csv.reader(file):
                card_instance = {
                    "group": card_info[0],
                    "function": card_info[1],
                    "value": card_info[2],
                    "name": card_info[3]
                }
                if card_instance["group"] == "c":
                    self.chance_list.append(card_instance)
                elif card_instance["group"] == "cc":
                    self.chest_list.append(card_instance)
        random.shuffle(self.chance_list)
        random.shuffle(self.chest_list)

    def draw_card(self, group):
        if group == "Chance":
            if not self.chance_list:
                self.load_cards()
            return self.chance_list.pop(0)
        elif group == "Community Chest":
            if not self.chest_list:
                self.load_cards()
            return self.chest_list.pop(0)
        else:
            return None

    def show_card(self):
        card_text = ""
        if self.game.current_player_location_property.colour == "Chance":
            draw_card = self.draw_card("Chance")
            if draw_card:
                match draw_card["function"]:
                    case "get":
                        self.game.current_player.update_money(int(draw_card["value"]))
                        card_text += f"Jogo da Sorte\n\n{draw_card['name']}\n\n{self.game.current_player.name} ganhou ${draw_card['value']}"
                    case "give":
                        self.game.current_player.update_money(-int(draw_card["value"]))
                        card_text += f"Jogo da Sorte\n\n{draw_card['name']}\n\n{self.game.current_player.name} pagou ${draw_card['value']}"
                    case "giveall":
                        self.game.current_player.update_money(-150)
                        for player in [self.game.player_1, self.game.player_2, self.game.player_3, self.game.player_4]:
                            if player != self.game.current_player:
                                player.update_money(50)
                        card_text += f"Jogo da Sorte\n\n{draw_card['name']}\n\n{self.game.current_player.name} pagou $150\nOutros jogadores receberam $50"
                    case "move":
                        self.game.current_player.update_location(1)
                        self.game.current_player.update_money(200)
                        card_text += f"Jogo da Sorte\n\n{draw_card['name']}\n\n{self.game.current_player.name} ganhou $200"
                        self.game.board.move_player(self.game.current_player, 675, 675)
            else:
                card_text += "Nenhuma carta disponível para 'Chance'"
        else:
            draw_card = self.draw_card("Community Chest")
            if draw_card:
                match draw_card["function"]:
                    case "get":
                        self.game.current_player.update_money(int(draw_card["value"]))
                        card_text += f"Baú da Comunidade\n\n{draw_card['name']}\n\n{self.game.current_player.name} recebeu ${draw_card['value']}"
                    case "give":
                        self.game.current_player.update_money(-int(draw_card["value"]))
                        card_text += f"Baú da Comunidade\n\n{draw_card['name']}\n\n{self.game.current_player.name} pagou ${draw_card['value']}"
                    case "move":
                        self.game.current_player.update_location(1)
                        self.game.current_player.update_money(200)
                        card_text += f"Baú da Comunidade\n\n{draw_card['name']}\n\n{self.game.current_player.name} recebeu $200"
                        self.game.board.move_player(self.game.current_player, 675, 675)
            else:
                card_text += "Nenhuma carta disponível para 'Baú da Comunidade'"

        if not self.game.end_check():
            self.game.card_display = tk.Label(self.game.screen, text=card_text, font=self.game.SMALL_FONT, borderwidth=0, bg=self.game.BG_LIGHT)
            self.game.card_display.place(height=160, width=250, x=360, y=500, anchor="s")
