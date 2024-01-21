from  src.items.item import Item

class MediumHealingPotion(Item):
    def __init__(self):
        super(MediumHealingPotion,self).__init__
        self.name = "Średnia mikstura lecznicza"
        self.description = "Najlepsza przyjaciółka wojownika"
        self.type = "Healing"
        self.use_value = 50 # This is the value that the item will do when used
        self.amount = 1
    
    