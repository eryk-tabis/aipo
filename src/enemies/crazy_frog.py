from src.enemies.enemy import Enemy

class CrazyFrog(Enemy):
    def __init__(self):
        super(CrazyFrog,self).__init__()
        self.name = "Szalona Żaba"
        self.hitPoints = 20
        self.stamina = 3
        self.strength = 8
        self.defense = 3
        self.agility = 3
