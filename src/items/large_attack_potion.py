from  src.items.item import Item

class LargemAttackPotion(Item):
    def __init__(self):
        super(LargemAttackPotion,self).__init__
        self.name = "Duża mikstura ataku"
        self.description = "Potęga prosto z butelki. Odejmuje 20 hp przeciwnikowi."
        self.type = "Damage"
        self.use_value = 20 # This is the value that the item will do when used
        self.amount = 1
    
    