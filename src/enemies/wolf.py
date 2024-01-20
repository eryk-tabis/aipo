from src.enemies.enemy import Enemy

class Wolf(Enemy):
    def __init__(self):
        super(Wolf,self).__init__()
        self.name = "Wilk"
        self.hitPoints = 15
        self.stamina = 9
        self.strength = 10
        self.defense = 2
        self.agility = 7
