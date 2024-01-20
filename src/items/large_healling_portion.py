from  src.items.item import Item

class LargeHealingPotion(Item):
    def __init__(self):
        super(LargeHealingPotion,self).__init__
        self.name = "Duża mikstura lecznicza"
        self.description = "Postawi na nogi nawet martwego"
        self.type = "leczenie"
        self.use_value = Item("Duża mikstura lecznicza","Postawi na nogi nawet martwego","leczenie",100,1) # This is the value that the item will do when used
        self.amount = 1
    
    