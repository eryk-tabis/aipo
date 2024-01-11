from src.weapons.weapon import Weapon

class MasterBow(Weapon):
    def __init__(self):
        self.name = "Master bow"
        self.damage = 20
        self.accuracy = 94
        self.type = "Range"

    
