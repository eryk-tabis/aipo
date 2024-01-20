from src.enemies.enemy import Enemy

class RatKing(Enemy):
    def __init__(self):
        super(RatKing,self).__init__()
        self.name = "Król Szczurów"
        self.hitPoints = 100
        self.stamina = 10
        self.strength = 12
        self.defense = 5
        self.agility = 3
