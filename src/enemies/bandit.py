from src.enemies.enemy import Enemy

class Bandit(Enemy):
    def __init__(self):
        super(Bandit,self).__init__()
        self.name = "Bandyta"
        self.hitPoints = 15
        self.stamina = 5
        self.strength = 7
        self.defense = 3
        self.agility = 2
