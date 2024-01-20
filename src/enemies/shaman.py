from src.enemies.enemy import Enemy

class Shaman(Enemy):
    def __init__(self):
        super(Shaman,self).__init__()
        self.name = "Szaman"
        self.hitPoints = 80
        self.stamina = 1
        self.strength = 6
        self.defense = 2
        self.agility = 3
