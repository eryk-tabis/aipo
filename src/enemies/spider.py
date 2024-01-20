from src.enemies.enemy import Enemy

class Spider(Enemy):
    def __init__(self):
        super(Spider,self).__init__()
        self.name = "Pająk"
        self.hitPoints = 10
        self.stamina = 5
        self.strength = 5
        self.defense = 2
        self.agility = 2
