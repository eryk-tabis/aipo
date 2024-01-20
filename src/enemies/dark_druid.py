from src.enemies.enemy import Enemy

class DarkDruid(Enemy):
    def __init__(self):
        super(DarkDruid,self).__init__()
        self.name = "Ciemny druid"
        self.hitPoints = 40
        self.stamina = 6
        self.strength = 7
        self.defense = 4
        self.agility = 5
