class Property:
    def __init__(self, name, price, colour, coords):
        self.name = name
        self.price = price
        self.colour = colour
        self.coords = coords
        self.owned_by = None
        self.rent = 0

    def set_owner(self, owner):
        self.owned_by = owner

    def set_rent(self, rent):
        self.rent = rent

    def get_info(self):
        return {
            "name": self.name,
            "price": self.price,
            "colour": self.colour,
            "coords": self.coords,
            "owned_by": self.owned_by,
            "rent": self.rent
        }
