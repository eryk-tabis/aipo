from src.enemies.enemy import Enemy

class RatKing(Enemy):
    def __init__(self):
        super(RatKing,self).__init__()
        self.name = "Król Szczurów"
        self.hp = 100
        self.strength = 12
        self.defense = 5
        self.agility = 40
