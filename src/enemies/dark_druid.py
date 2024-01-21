from src.enemies.enemy import Enemy

class DarkDruid(Enemy):
    def __init__(self):
        super(DarkDruid,self).__init__()
        self.name = "Ciemny druid"
        self.hp = 40
        self.damage = 7
        self.defense = 4
        self.agility = 50
