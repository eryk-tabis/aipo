from src.enemies.enemy import Enemy

class Assasin(Enemy):
    def __init__(self):
        super(Assasin,self).__init__()
        self.name = "Zabójca"
        self.hp = 30
        self.damage = 10
        self.defense = 1
        self.agility = 30
