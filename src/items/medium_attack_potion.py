from  src.items.item import Item

class MediumAttackPotion(Item):
    def __init__(self):
        super(MediumAttackPotion,self).__init__
        self.name = "Średnia mikstura ataku"
        self.description = "Siła pozwalająca wyrywać drzewa z korzeniami"
        self.type = "Damage"
        self.use_value = 10 # This is the value that the item will do when used
        self.amount = 1
    
    