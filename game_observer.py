from observer import Observer

class GameObserver(Observer):
    def update(self, data):
        if data['event'] == 'dice_roll':
            print(f"Dice rolled: {data['dice_1']} and {data['dice_2']} (total: {data['roll_no']})")
        elif data['event'] == 'player_move':
            print(f"Player {data['player_name']} moved to {data['property_name']}")
        elif data['event'] == 'property_purchase':
            print(f"Player {data['player_name']} purchased {data['property_name']} for ${data['price']}")
        elif data['event'] == 'pay_rent':
            print(f"Player {data['player_name']} paid ${data['rent']} rent to {data['owner_name']}")
        elif data['event'] == 'pay_tax':
            print(f"Player {data['player_name']} paid ${data['tax']} in taxes")
        elif data['event'] == 'draw_card':
            print(f"Player {data['player_name']} drew a card: {data['card_text']}")
        elif data['event'] == 'go_to_jail':
            print(f"Player {data['player_name']} was sent to jail")
        elif data['event'] == 'pay_fine':
            print(f"Player {data['player_name']} paid a $50 fine")
        elif data['event'] == 'receive_salary':
            print(f"Player {data['player_name']} received $200 salary")
