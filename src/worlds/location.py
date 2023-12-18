class Location:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.locations_nearby = {}
        self.items = []
        self.enemies = []

    def add_item(self, item):
        self.items.append(item)

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def add_location(self, location, direction):
        self.locations_nearby[direction] = location

    def remove_item(self, item):
        self.items.remove(item)


    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item

    def get_enemy(self, enemy_name):
        for enemy in self.enemies:
            if enemy.name == enemy_name:
                return enemy

    def get_location(self, direction):
        return self.locations_nearby.get(direction)

    def get_items(self):
        return self.items

    def get_enemies(self):
        return self.enemies

    def get_locations_nearby(self):
        return self.locations_nearby
