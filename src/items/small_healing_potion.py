from  src.items.item import Item

class SmallHealingPotion(Item):
    def __init__(self):
        super(SmallHealingPotion,self).__init__
        self.name = "Mała mikstura lecznicza"
        self.description = "mała i poręczna na ciężkie boje"
        self.type = "leczenie"
        self.use_value = Item("Mała mikstura lecznicza","mała i poręczna na ciężkie boje","leczenie",20,1) # This is the value that the item will do when used
        self.amount = 1
    
    