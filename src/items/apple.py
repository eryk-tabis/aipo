from  src.items.item import Item

class Apple(Item):
    def __init__(self):
        super(Apple,self).__init__
        self.name = "Jabłko"
        self.description = "Pyszne słodkie i soczyste"
        self.type = "Healing"
        self.use_value = Item("Jabłko","Pyszne słodkie i soczyste","leczenie",5,1) # This is the value that the item will do when used
        self.amount = 1
    
    