from src.enemies.enemy import Enemy

class Wolf(Enemy):
    def __init__(self):
        super(Wolf,self).__init__()
        self.name = "Wilk"
        self.hp = 15
        self.damage = 10
        self.defense = 2
        self.agility = 70
