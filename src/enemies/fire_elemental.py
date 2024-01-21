from src.enemies.enemy import Enemy

class FireElemental(Enemy):
    def __init__(self):
        super(FireElemental,self).__init__()
        self.name = "Żywiołak Ognia"
        self.hp = 60
        self.damage = 10
        self.defense = 4
        self.agility = 40
