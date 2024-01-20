from src.enemies.enemy import Enemy

class FireElemental(Enemy):
    def __init__(self):
        super(FireElemental,self).__init__()
        self.name = "Żywiołak Ognia"
        self.hitPoints = 60
        self.stamina = 7
        self.strength = 10
        self.defense = 4
        self.agility = 4
