from src.enemies.enemy import Enemy

class Boar(Enemy):
    def __init__(self):
        super(Boar,self).__init__()
        self.name = "Dzik"
        self.hitPoints = 5
        self.stamina = 5
        self.strength = 10
        self.defense = 4
        self.agility = 2
