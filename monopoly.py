import csv
import itertools
import random
from ctypes import windll

from PIL import Image, ImageTk
import tkextrafont
import tkinter as tk

from Cards import Cards
from Property import Property
from gui.press_any_key_screen import menu_screen_display
from observer import Subject
from game_observer import GameObserver
from Player.player import Player
from Player.player_human import PlayerHuman
from Player.player_ia import PlayerIA
from Dice import Dice
from Board import Board


class Monopoly(Subject):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Monopoly, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            super().__init__()

            self.root = tk.Tk()
            self.root.geometry("1280x720")
            self.root.title("Monopoly")
            self.root.iconbitmap(default=r"textures/logo.ico")
            self.root.resizable(False, False)

            self.BIG_FONT = tkextrafont.Font(file=r"fonts/big_font.ttf", family="Kabel Bd", size=20)
            self.FONT = tkextrafont.Font(file=r"fonts/font.ttf", family="Kabel Bd", size=18)
            self.SMALL_FONT = tkextrafont.Font(file=r"fonts/small_font.ttf", family="Kabel Bd", size=12)

            self.cards = Cards(self)
            self.dice = Dice(self)

            self.tokens = [
                r"textures/tokens/black-token.png",
                r"textures/tokens/blue-token.png",
                r"textures/tokens/brown-token.png",
                r"textures/tokens/green-token.png",
                r"textures/tokens/light_green-token.png",
                r"textures/tokens/purple-token.png",
                r"textures/tokens/red-token.png",
                r"textures/tokens/white-token.png",
                r"textures/tokens/yellow-token.png",
                r"textures/tokens/pink-token.png",
            ]
            self.display_tokens = [
                r"textures/tokens/black.png",
                r"textures/tokens/blue.png",
                r"textures/tokens/brown.png",
                r"textures/tokens/green.png",
                r"textures/tokens/light_green.png",
                r"textures/tokens/purple.png",
                r"textures/tokens/red.png",
                r"textures/tokens/white.png",
                r"textures/tokens/yellow.png",
                r"textures/tokens/pink.png",
            ]

            self.player_1 = PlayerHuman("Jogador 1")
            self.player_2 = PlayerIA("Jogador 2")
            self.player_3 = PlayerIA("Jogador 3")
            self.player_4 = PlayerIA("Jogador 4")

            self.BG_DARK = "#0E2C4F"
            self.BG_LIGHT = "#B9CEB5"
            self.BG_BOARD = "#85E7A7"
            self.BG_BUTTON = "#495D66"

            windll.shcore.SetProcessDpiAwareness(1)

            self.title_image = ImageTk.PhotoImage(file=r"textures/title.png")

            self.end_turn_button = None
            self.current_player_display = None
            self.salary_display = None
            self.current_player_landing = None
            self.property_choice_display = None
            self.action_display = None
            self.card_display = None

            menu_screen_display(self)
            
            self.initialized = True

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_game(self):
        try:
            self.player_1.name = self.player_1_entry.get()
            self.player_2.name = self.player_2_entry.get()
            self.player_3.name = self.player_3_entry.get()
            self.player_4.name = self.player_4_entry.get()
            self.select_screen.destroy()
        except:
            pass
        try:
            self.title_screen.destroy()
        except AttributeError:
            pass

        for player in (self.player_1, self.player_2, self.player_3, self.player_4):
            player.update_location(1)
            player.update_money(1500 - player.money)
            player.properties.clear()
            player.set_turn(False)

        self.screen = tk.Frame(self.root, background="black")
        self.screen.pack(fill="both", expand=True)

        self.board = Board(self)

        button_background_image = ImageTk.PhotoImage(Image.new("RGB", (560, 720), self.BG_BUTTON))
        button_background = tk.Label(self.screen, image=button_background_image, borderwidth=0)
        button_background.place(relx=1, rely=0, anchor="ne")

        self.close_player_button_image = ImageTk.PhotoImage(file=r"textures/close.png")

        try:
            self.player_1.token_display_image = self.player_1_image
            self.player_1.token_image = ImageTk.PhotoImage(file=self.tokens[self.player_1_index])
            self.player_2.token_display_image = self.player_2_image
            self.player_2.token_image = ImageTk.PhotoImage(file=self.tokens[self.player_2_index])
            self.player_3.token_display_image = self.player_3_image
            self.player_3.token_image = ImageTk.PhotoImage(file=self.tokens[self.player_3_index])
            self.player_4.token_display_image = self.player_4_image
            self.player_4.token_image = ImageTk.PhotoImage(file=self.tokens[self.player_4_index])
        except AttributeError:
            pass

        self.p1_token_display = tk.Label(
            self.screen, image=self.player_1.token_display_image, borderwidth=0, bg=self.BG_BUTTON
        )
        self.p1_token_display.place(x=871, y=140, anchor="s")
        p1_button = tk.Button(
            self.screen,
            text=self.player_1.name,
            font=self.FONT,
            compound="center",
            image=self.button_image,
            bg=self.BG_BUTTON,
            activebackground=self.BG_BUTTON,
            borderwidth=0,
            command=lambda: self.display_player_info(self.player_1),
        )
        p1_button.place(width=170, height=62, x=786, y=140, anchor="nw")
        self.player_1_money_token = tk.Label(
            self.screen, image=self.player_1.token_image, borderwidth=0, bg=self.BG_BUTTON
        )
        self.player_1_money_token.place(x=775, y=500, anchor="nw")
        self.player_1_money = tk.Label(
            self.screen, text=f": ${self.player_1.money}", borderwidth=0, font=self.FONT, bg=self.BG_BUTTON
        )
        self.player_1_money.place(x=830, y=508, anchor="nw")

        self.p2_token_display = tk.Label(
            self.screen, image=self.player_2.token_display_image, borderwidth=0, bg=self.BG_BUTTON
        )
        self.p2_token_display.place(x=1139, y=140, anchor="s")
        p2_button = tk.Button(
            self.screen,
            text=self.player_2.name,
            font=self.FONT,
            compound="center",
            image=self.button_image,
            bg=self.BG_BUTTON,
            activebackground=self.BG_BUTTON,
            borderwidth=0,
            command=lambda: self.display_player_info(self.player_2),
        )
        p2_button.place(width=170, height=62, x=1224, y=140, anchor="ne")
        self.player_2_money_token = tk.Label(
            self.screen, image=self.player_2.token_image, borderwidth=0, bg=self.BG_BUTTON
        )
        self.player_2_money_token.place(x=775, y=548, anchor="nw")
        self.player_2_money = tk.Label(
            self.screen, text=f": ${self.player_2.money}", borderwidth=0, font=self.FONT, bg=self.BG_BUTTON
        )
        self.player_2_money.place(x=830, y=556, anchor="nw")

        self.p3_token_display = tk.Label(
            self.screen, image=self.player_3.token_display_image, borderwidth=0, bg=self.BG_BUTTON
        )
        self.p3_token_display.place(x=871, y=350, anchor="s")
        p3_button = tk.Button(
            self.screen,
            text=self.player_3.name,
            font=self.FONT,
            compound="center",
            image=self.button_image,
            bg=self.BG_BUTTON,
            activebackground=self.BG_BUTTON,
            borderwidth=0,
            command=lambda: self.display_player_info(self.player_3),
        )
        p3_button.place(width=170, height=62, x=786, y=350, anchor="nw")
        self.player_3_money_token = tk.Label(
            self.screen, image=self.player_3.token_image, borderwidth=0, bg=self.BG_BUTTON
        )
        self.player_3_money_token.place(x=775, y=596, anchor="nw")
        self.player_3_money = tk.Label(
                        self.screen, text=f": ${self.player_3.money}", borderwidth=0, font=self.FONT, bg=self.BG_BUTTON
        )
        self.player_3_money.place(x=830, y=604, anchor="nw")

        self.p4_token_display = tk.Label(
            self.screen, image=self.player_4.token_display_image, borderwidth=0, bg=self.BG_BUTTON
        )
        self.p4_token_display.place(x=1139, y=350, anchor="s")
        p4_button = tk.Button(
            self.screen,
            text=self.player_4.name,
            font=self.FONT,
            compound="center",
            image=self.button_image,
            bg=self.BG_BUTTON,
            activebackground=self.BG_BUTTON,
            borderwidth=0,
            command=lambda: self.display_player_info(self.player_4),
        )
        p4_button.place(width=170, height=62, x=1224, y=350, anchor="ne")
        self.player_4_money_token = tk.Label(
            self.screen, image=self.player_4.token_image, borderwidth=0, bg=self.BG_BUTTON
        )
        self.player_4_money_token.place(x=775, y=644, anchor="nw")
        self.player_4_money = tk.Label(
            self.screen, text=f": ${self.player_4.money}", borderwidth=0, font=self.FONT, bg=self.BG_BUTTON
        )
        self.player_4_money.place(x=830, y=652, anchor="nw")

        self.player_1.token = self.board.board.create_image(651, 650, image=self.player_1.token_image, anchor="center")
        self.player_2.token = self.board.board.create_image(651, 695, image=self.player_2.token_image, anchor="center")
        self.player_3.token = self.board.board.create_image(696, 650, image=self.player_3.token_image, anchor="center")
        self.player_4.token = self.board.board.create_image(696, 695, image=self.player_4.token_image, anchor="center")

        self.player_loop = itertools.cycle([self.player_1, self.player_2, self.player_3, self.player_4])
        self.player_turn_init(next(self.player_loop))

        self.root.mainloop()

    def display_player_info(self, player):
        try:
            self.player_info.destroy()
            self.close_player_button.destroy()
        except AttributeError:
            pass

        player_info_text = f"{player.name}\n${player.money}\n\n"
        player_info_text += "\n".join([title.get_info()["name"] for title in player.properties])

        self.player_info = tk.Label(self.screen, text=player_info_text, borderwidth=0, font=self.SMALL_FONT, bg=self.BG_LIGHT)
        self.player_info.place(height=280, width=250, x=360, y=360, anchor="center")

        self.close_player_button = tk.Button(
            self.screen,
            borderwidth=0,
            image=self.close_player_button_image,
            bg=self.BG_LIGHT,
            activebackground=self.BG_LIGHT,
            command=lambda: (self.player_info.destroy(), self.close_player_button.destroy()),
        )
        self.close_player_button.place(x=460, y=245, anchor="center")

    def player_turn_init(self, player):
        self.current_player = player
        self.current_player.set_turn(True)

        if self.current_player_display:
            self.current_player_display.destroy()

        self.current_player_display = tk.Label(
            self.screen, text=f"Vez de {self.current_player.name}", font=self.BIG_FONT, borderwidth=0, bg=self.BG_BUTTON
        )
        self.current_player_display.place(width=560, height=60, x=1000, y=460, anchor="center")

        if player.type == "human":
            dice_button = tk.Button(
                self.screen,
                image=self.dice.dice_image,
                borderwidth=0,
                bg=self.BG_BUTTON,
                activebackground=self.BG_BUTTON,
                command=lambda: (self.end_turn_display(), self.player_turn(), dice_button.destroy()),
            )
            dice_button.place(x=1032, y=532, anchor="nw")
        else:
            self.root.after(1000, self.player_turn)

    def end_turn_display(self):
        if self.end_turn_button:
            self.end_turn_button.destroy()

        self.end_turn_button = tk.Button(
            self.screen,
            text="TERMINAR",
            font=self.FONT,
            borderwidth=0,
            compound="center",
            image=self.button_image,
            bg=self.BG_BUTTON,
            activebackground=self.BG_BUTTON,
            command=lambda: (self.end_turn_func(), self.end_turn_button.destroy()),
        )
        self.end_turn_button.place(width=170, height=62, x=1012, y=615, anchor="nw")

    def player_turn(self):
        dice_1, dice_2 = self.dice.roll()
        self.roll_no = dice_1 + dice_2
        self.notify_observers({"event": "dice_roll", "dice_1": dice_1, "dice_2": dice_2, "roll_no": self.roll_no})

        if self.current_player.location + self.roll_no > 40:
            roll_difference = 40 - (self.current_player.location + self.roll_no)
            self.current_player.update_location(-roll_difference)
            self.clear_display(self.salary_display)
            self.salary_display = tk.Label(
                self.screen,
                text=f"{self.current_player.name} Recebeu $200 de salário",
                borderwidth=0,
                bg=self.BG_BOARD,
                font=self.SMALL_FONT,
            )
            self.salary_display.place(x=360, y=300, anchor="n")
            self.current_player.update_money(200)
            self.update_money()
        else:
            self.current_player.update_location(self.current_player.location + self.roll_no)
        self.current_player_location_property = self.board.property_locations[self.current_player.location]

        x, y = self.current_player_location_property.coords
        self.board.move_player(self.current_player, x, y)
        self.clear_display(self.current_player_landing)
        current_player_landing_text = f"{self.current_player.name} Tirou {self.roll_no}\n&\nChegou em {self.current_player_location_property.name}"
        self.current_player_landing = tk.Label(self.screen, text=current_player_landing_text, bg=self.BG_BOARD, borderwidth=0, font=self.SMALL_FONT)
        self.current_player_landing.place(x=360, y=145, anchor="n")

        if self.current_player_location_property.colour not in [
            "Go",
            "Community Chest",
            "Chance",
            "Tax",
            "Jail",
            "Go to Jail",
            "Free Parking",
        ]:
            if self.current_player_location_property.owned_by not in [self.player_1, self.player_2, self.player_3, self.player_4]:
                if self.current_player_location_property.price <= self.current_player.money:
                    self.clear_display(self.property_choice_display)
                    if self.current_player.type == "human":
                        self.property_choice_display = tk.Button(
                            self.screen,
                            text=f"COMPRAR\n${self.current_player_location_property.price}",
                            compound="center",
                            image=self.button_image,
                            bg=self.BG_BUTTON,
                            activebackground=self.BG_BUTTON,
                            borderwidth=0,
                            font=self.FONT,
                            command=lambda: (self.buy_property(), self.property_choice_display.destroy()),
                        )
                        self.property_choice_display.place(width=270, height=62, x=962, y=515, anchor="nw")
                    else:
                        if random.randint(0, 4):
                            self.root.after(500, self.buy_property)

            elif self.current_player_location_property.colour == "Utility":
                if self.current_player != self.current_player_location_property.owned_by:
                    self.pay_utility()
            else:
                if self.current_player != self.current_player_location_property.owned_by:
                    self.pay_rent()
        elif self.current_player_location_property.colour == "Tax":
            self.pay_tax()
        elif self.current_player_location_property.colour in ["Chance", "Community Chest"]:
            self.cards.show_card()  
        elif self.current_player_location_property.colour == "Go to Jail":
            self.current_player.update_location(11)
            self.clear_display(self.action_display)
            self.action_display = tk.Label(
                self.screen, text=f"{self.current_player.name} foi para a prisão", borderwidth=0, bg=self.BG_BOARD, font=self.SMALL_FONT
            )
            try:
                self.player_info.destroy()
                self.close_player_button.destroy()
            except AttributeError:
                pass
            self.action_display.place(x=360, y=260, anchor="n")
            self.board.move_player(self.current_player, 63, 660)

            if self.current_player.type == "human":
                fine_display = tk.Button(
                    self.screen,
                    text=f"FIANÇA: $50",
                    compound="center",
                    image=self.button_image,
                    bg=self.BG_BUTTON,
                    activebackground=self.BG_BUTTON,
                    borderwidth=0,
                    font=self.FONT,
                    command=lambda: (self.pay_fine(), fine_display.destroy()),
                )
                fine_display.place(width=170, height=62, x=1012, y=515, anchor="nw")
                self.end_turn_button.destroy()
            else:
                self.root.after(500, self.pay_fine)

        if self.current_player.type == "npc":
            self.root.after(1500, self.end_turn_func)

    def end_turn_func(self):
        self.current_player.set_turn(False)
        next_player = next(self.player_loop)

        attributes_to_destroy = [
            "current_player_landing",
            "salary_display",
            "property_choice_display",
            "action_display",
            "card_display",
        ]

        for attribute in attributes_to_destroy:
            self.clear_display(getattr(self, attribute))

        self.player_turn_init(next_player)

    def clear_display(self, widget):
        if widget:
            widget.destroy()

    def buy_property(self):
        self.current_player.update_money(-self.current_player_location_property.price)
        if not self.end_check():
            self.current_player.add_property(self.current_player_location_property)
            self.current_player_location_property.set_owner(self.current_player)

            self.clear_display(self.action_display)
            self.action_display = tk.Label(
                self.screen,
                text=f"{self.current_player.name} Comprou {self.current_player_location_property.name} por ${self.current_player_location_property.price}",
                borderwidth=0,
                bg=self.BG_BOARD,
                font=self.SMALL_FONT,
            )
            try:
                self.player_info.destroy()
                self.close_player_button.destroy()
            except AttributeError:
                pass
            self.action_display.place(x=360, y=260, anchor="n")

            set_colour = self.current_player_location_property.colour
            set_number = 0
            rent = 0
            for title in self.current_player.properties:
                if title.colour == set_colour:
                    set_number += 1
            if set_colour == "Station":
                match set_number:
                    case 1:
                        rent = 75
                    case 2:
                        rent = 100
                    case 3:
                        rent = 125
                    case 4:
                        rent = 150
            else:
                match set_number:
                    case 1:
                        rent = self.current_player_location_property.price // 2
                    case 2:
                        rent = self.current_player_location_property.price
                    case 3:
                        rent = self.current_player_location_property.price * 2

            for title in self.current_player.properties:
                if title.colour == set_colour:
                    title.set_rent(rent)

    def pay_rent(self):
        self.current_player.update_money(-self.current_player_location_property.rent)
        if not self.end_check():
            self.current_player_location_property.owned_by.update_money(self.current_player_location_property.rent)
            self.update_money()
            self.clear_display(self.action_display)
            self.action_display = tk.Label(
                self.screen,
                text=f"{self.current_player.name} Pagou ${self.current_player_location_property.rent} para {self.current_player_location_property.owned_by.name}",
                borderwidth=0,
                bg=self.BG_BOARD,
                font=self.SMALL_FONT,
            )
            try:
                self.player_info.destroy()
                self.close_player_button.destroy()
            except AttributeError:
                pass
            self.action_display.place(x=360, y=260, anchor="n")

    def pay_tax(self):
        self.current_player.update_money(-self.current_player_location_property.price)
        if not self.end_check():
            self.clear_display(self.action_display)
            self.action_display = tk.Label(
                self.screen,
                text=f"{self.current_player.name} Pagou ${self.current_player_location_property.price} de taxa",
                borderwidth=0,
                bg=self.BG_BOARD,
                font=self.SMALL_FONT,
            )
            try:
                self.player_info.destroy()
                self.close_player_button.destroy()
            except AttributeError:
                pass
            self.action_display.place(x=360, y=260, anchor="n")

    def pay_utility(self):
        utility_count = 0
        for title in self.current_player_location_property.owned_by.properties:
            if title.colour == "Utility":
                utility_count += 1
        if utility_count == 1:
            self.current_player.update_money(-self.roll_no * 4)
            if not self.end_check():
                self.current_player_location_property.owned_by.update_money(self.roll_no * 4)
                self.update_money()
                self.clear_display(self.action_display)
                self.action_display = tk.Label(
                    self.screen,
                    text=f"{self.current_player.name} Pagou ${self.roll_no * 4} para {self.current_player_location_property.owned_by.name}",
                    borderwidth=0,
                    bg=self.BG_BOARD,
                    font=self.SMALL_FONT,
                )
                try:
                    self.player_info.destroy()
                    self.close_player_button.destroy()
                except AttributeError:
                    pass
                self.action_display.place(x=360, y=260, anchor="n")

        elif utility_count == 2:
            self.current_player.update_money(-self.roll_no * 10)
            if not self.end_check():
                self.current_player_location_property.owned_by.update_money(self.roll_no * 10)
                self.update_money()
                self.clear_display(self.action_display)
                self.action_display = tk.Label(
                    self.screen,
                    text=f"{self.current_player.name} Pagou ${self.roll_no * 10} para {self.current_player_location_property.owned_by.name}",
                    borderwidth=0,
                    bg=self.BG_BOARD,
                    font=self.SMALL_FONT,
                )
                try:
                    self.player_info.destroy()
                    self.close_player_button.destroy()
                except AttributeError:
                    pass
                self.action_display.place(x=360, y=260, anchor="n")

    def pay_fine(self):
        self.current_player.update_money(-50)
        if not self.end_check():
            self.clear_display(self.action_display)
            self.action_display = tk.Label(
                self.screen,
                text=f"{self.current_player.name} Pagou $50 de fiança",
                borderwidth=0,
                bg=self.BG_BOARD,
                font=self.SMALL_FONT,
            )
            try:
                self.player_info.destroy()
                self.close_player_button.destroy()
            except AttributeError:
                pass
            self.action_display.place(x=360, y=260, anchor="n")
            if self.current_player.type == "human":
                self.end_turn_display()

    def update_money(self):
        self.player_1_money.config(text=f": ${self.player_1.money}")
        self.player_2_money.config(text=f": ${self.player_2.money}")
        self.player_3_money.config(text=f": ${self.player_3.money}")
        self.player_4_money.config(text=f": ${self.player_4.money}")

    def end_check(self):
        if self.current_player.money < 0:
            self.current_player.money = 0
            self.update_money()
            if self.end_turn_button:
                self.end_turn_button.destroy()
            final_player_list = [self.player_1, self.player_2, self.player_3, self.player_4]

            final_player_list.remove(self.current_player)
            self.current_player.type = "human"
            final_player_money_list = []
            for player in final_player_list:
                player.type = "human"
                money = player.money
                for title in player.properties:
                    money += title.get_info().get("rent", 0)
                player.money = money
                final_player_money_list.append(player.money)
            winner = final_player_list[final_player_money_list.index(max(final_player_money_list))]

            end_text = f"{self.current_player.name} está falido\n\n{winner.name} venceu o jogo\n\nPatrimônio líquido:\n\n"
            sorted_player_list = sorted([self.player_1, self.player_2, self.player_3, self.player_4], key=lambda player: player.money, reverse=True)
            for player in sorted_player_list:
                end_text += f"{player.name}: ${player.money}\n"
            end_screen = tk.Label(self.screen, text=end_text, borderwidth=0, font=self.SMALL_FONT, bg=self.BG_LIGHT)
            end_screen.place(height=280, width=250, x=360, y=360, anchor="center")
            return True
        else:
            self.update_money()
            return False

if __name__ == "__main__":
    game = Monopoly()
    observer = GameObserver()
    game.add_observer(observer)
    game.root.mainloop()