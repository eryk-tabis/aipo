from  src.items.item import Item

class SmallAttackPotion(Item):
    def __init__(self):
        super(SmallAttackPotion,self).__init__
        self.name = "Mała mikstura ataku"
        self.description = "Daje uczucie swądu w dłoniach"
        self.type = "Damage"
        self.use_value = 5 # This is the value that the item will do when used
        self.amount = 1
    
    