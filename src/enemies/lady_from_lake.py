from src.enemies.enemy import Enemy

class LadyOfTheLake(Enemy):
    def __init__(self):
        super(LadyOfTheLake,self).__init__()
        self.name = "Pani Jeziora"
        self.hp = 200
        self.damage = 30
        self.defense = 5
        self.agility = 50
