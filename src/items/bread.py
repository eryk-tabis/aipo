from  src.items.item import Item

class Bread(Item):
    def __init__(self):
        super(Bread,self).__init__
        self.name = "Chleb"
        self.description = "Prosta strawa dla wędrowca. Dodaje 10 hp"
        self.type = "Healing"
        self.use_value = 10 # This is the value that the item will do when used
        self.amount = 1
    
    