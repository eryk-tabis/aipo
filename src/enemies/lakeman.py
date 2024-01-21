from src.enemies.enemy import Enemy

class LakeMan(Enemy):
    def __init__(self):
        super(LakeMan,self).__init__()
        self.name = "Jeziorak"
        self.hp = 40
        self.strength = 4
        self.defense = 10
        self.agility = 70
