from src.enemies.enemy import Enemy

class Rat(Enemy):
    def __init__(self):
        super(Rat,self).__init__()
        self.name = "Szczur"
        self.hp = 25
        self.strength = 5
        self.defense = 3
        self.agility = 25
