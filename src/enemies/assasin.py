from src.enemies.enemy import Enemy

class Assasin(Enemy):
    def __init__(self):
        super(Assasin,self).__init__()
        self.name = "Zabójca"
        self.hitPoints = 30
        self.stamina = 6
        self.strength = 10
        self.defense = 1
        self.agility = 3
