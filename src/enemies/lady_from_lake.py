from src.enemies.enemy import Enemy

class Spider(Enemy):
    def __init__(self):
        super(Spider,self).__init__()
        self.name = "Pani Jeziora"
        self.hp = 200
        self.strength = 30
        self.defense = 5
        self.agility = 50
