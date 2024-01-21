from src.enemies.enemy import Enemy

class Spider(Enemy):
    def __init__(self):
        super(Spider,self).__init__()
        self.name = "Pająk"
        self.hp = 10
        self.damage = 5
        self.defense = 2
        self.agility = 30
