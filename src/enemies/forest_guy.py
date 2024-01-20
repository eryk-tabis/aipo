from src.enemies.enemy import Enemy

class ForestGuy(Enemy):
    def __init__(self):
        super(ForestGuy,self).__init__()
        self.name = "Leśny Dziad"
        self.hitPoints = 80
        self.stamina = 2
        self.strength = 2
        self.defense = 10
        self.agility = 2
