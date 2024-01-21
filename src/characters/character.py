from random import randint

class Character():
    def __init__(self, **kwargs):
        self.name = None
        self.inventory = {}
        super(Character, self).__init__()
    
    def add_to_inventory(self, item: object):
        if self.inventory.get(item.name):
            self.inventory[item.name]["amount"] += item.amount
        else:
            self.inventory.update({item.name: {"item": item, "amount": item.amount}})