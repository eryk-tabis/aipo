from  src.items.item import Item

class Apple(Item):
    def __init__(self):
        super(Apple,self).__init__
        self.name = "Jabłko"
        self.description = "Pyszne słodkie i soczyste. Dodaje 5 hp"
        self.type = "Healing"
        self.use_value = 5 # This is the value that the item will do when used
        self.amount = 1
    
    