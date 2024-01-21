from src.enemies.enemy import Enemy

class Bandit(Enemy):
    def __init__(self):
        super(Bandit,self).__init__()
        self.name = "Bandyta"
        self.hp = 15
        self.damage = 7
        self.defense = 3
        self.agility = 60
