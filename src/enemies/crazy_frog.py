from src.enemies.enemy import Enemy

class CrazyFrog(Enemy):
    def __init__(self):
        super(CrazyFrog,self).__init__()
        self.name = "Szalona Żaba"
        self.hp = 20
        self.strength = 8
        self.defense = 3
        self.agility = 35
