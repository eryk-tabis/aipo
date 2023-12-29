
def create_player(name: str, character_class: object, race_class: object):
    class Player(character_class, race_class):
        def __init__(self, name: str):
            super(character_class, self).__init__()
            super(race_class, self).__init__()
            self.name = name

        def show_items_in_inventory(self):
            return self.inventory.keys()

        def add_to_inventory(self, item: object):
            if self.inventory.get(item.name):
                self.inventory[item.name]["amount"] += item.amount
            else:
                self.inventory.update({item.name: {"item": item, "amount": item.amount}})
        def get_item_from_inventory(self, item_name: str):
            return self.inventory.get(item_name)
        def remove_from_inventory(self, item: object):
            if self.inventory.get(item.name):
                self.inventory[item.name]["amount"] -= item.amount
                if self.inventory[item.name]["amount"] <= 0:
                    del self.inventory[item.name]

    return Player
