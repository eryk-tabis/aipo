from  src.items.item import Item

class LargeHealingPotion(Item):
    def __init__(self):
        super(LargeHealingPotion,self).__init__
        self.name = "Duża mikstura lecznicza"
        self.description = "Postawi na nogi nawet martwego. Heals 100 hp."
        self.type = "Healing"
        self.use_value = 100 # This is the value that the item will do when used
        self.amount = 1
    
    