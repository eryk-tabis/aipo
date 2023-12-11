class Location:
    def __init__(self, name, description, items=None, enemies=None):
        self.name = name
        self.description = description
        self.locations_nearby = {}
        self.items = items or []
        self.enemies = enemies or []
