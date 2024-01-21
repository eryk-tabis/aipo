from  src.items.item import Item

class Bread(Item):
    def __init__(self):
        super(Bread,self).__init__
        self.name = "Chleb"
        self.description = "Prosta strawa dla wędrowca"
        self.type = "Healing"
        self.use_value = Item("Chleb","Prosta strawa dla wędrowca","leczenie",10,1) # This is the value that the item will do when used
        self.amount = 1
    
    