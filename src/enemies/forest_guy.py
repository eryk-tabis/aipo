from src.enemies.enemy import Enemy

class ForestGuy(Enemy):
    def __init__(self):
        super(ForestGuy,self).__init__()
        self.name = "Leśny Dziad"
        self.hp = 80
        self.damage = 5
        self.defense = 10
        self.agility = 25
