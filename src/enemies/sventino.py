from src.enemies.enemy import Enemy

class Sventino(Enemy):
    def __init__(self):
        super(Sventino,self).__init__()
        self.name = "Sventino"
        self.hp = 300
        self.damage = 40
        self.defense = 10
        self.agility = 100
