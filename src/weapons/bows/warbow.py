from src.weapons.weapon import Weapon

class Warbow(Weapon):
    def __init__(self):
        self.name = "War bow"
        self.damage = 16
        self.accuracy = 86
        self.type = "Range"

    
