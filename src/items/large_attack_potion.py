from  src.items.item import Item

class LargemAttackPotion(Item):
    def __init__(self):
        super(LargemAttackPotion,self).__init__
        self.name = "Duża mikstura ataku"
        self.description = "Potęga prosto z butelki"
        self.type = "atak"
        self.use_value = Item("Duża mikstura ataku","Potęga prosto z butelki","atak",20,1) # This is the value that the item will do when used
        self.amount = 1
    
    