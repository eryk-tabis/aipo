from src.weapons.weapon import Weapon

class HolyBow(Weapon):
    def __init__(self):
        self.name = "Holy bow"
        self.damage = 28
        self.accuracy = 100
        self.type = "Range"

    
