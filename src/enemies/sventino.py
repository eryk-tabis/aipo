from src.enemies.enemy import Enemy

class Sventino(Enemy):
    def __init__(self):
        super(Sventino,self).__init__()
        self.name = "Sventino"
        self.hitPoints = 300
        self.stamina = 60
        self.strength = 40
        self.defense = 10
        self.agility = 10
