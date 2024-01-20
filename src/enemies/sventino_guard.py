from src.enemies.enemy import Enemy

class SventinoGuard(Enemy):
    def __init__(self):
        super(SventinoGuard,self).__init__()
        self.name = "Strażnik Sventino"
        self.hitPoints = 100
        self.stamina = 5
        self.strength = 8
        self.defense = 5
        self.agility = 1
