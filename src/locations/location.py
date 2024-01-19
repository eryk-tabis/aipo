class Location:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.locations_nearby = {}
        self.items = []
        self.enemies = []
        self.cutseneces = []

    def add_item(self, item):
        self.items.append(item)

    def add_enemy(self, enemy):
        self.enemies.append(enemy)
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

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
    def get_description(self):
        return self.description
    def get_location(self, direction):
        return self.locations_nearby.get(direction)
    def get_items(self):
        return self.items

    def get_enemies(self):
        return self.enemies

    def _get_locations_nearby(self):
        return self.locations_nearby
    def get_locations_nearby(self):
        prompt = "Możesz iść tutaj:"
        for direction in self._get_locations_nearby().keys():
            prompt += f"\n - " + direction
        return prompt
    def add_cutscene(self, cutscene):
        self.cutseneces.append(cutscene)
    def get_cutsceneses(self):
        return self.cutseneces or None
    def remove_cutscene(self, cutscene):
        self.cutseneces.remove(cutscene)