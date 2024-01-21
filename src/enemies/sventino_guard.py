from src.enemies.enemy import Enemy

class SventinoGuard(Enemy):
    def __init__(self):
        super(SventinoGuard,self).__init__()
        self.name = "Strażnik Sventino"
        self.hp = 100
        self.damage = 8
        self.defense = 5
        self.agility = 60
