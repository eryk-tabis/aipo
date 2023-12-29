class Item:
    def __init__(self, name, description, type, use_value,amount):
        self.name = name
        self.description = description
        self.type = type
        self.use_value = use_value # This is the value that the item will do when used
        self.amount = amount

    def __str__(self):
        return f"{self.name}"
