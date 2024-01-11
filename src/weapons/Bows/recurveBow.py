from src.weapons.weapon import Weapon

class Recurvebow(Weapon):
    def __init__(self):
        self.name = "Bow"
        self.damage = 16
        self.accuracy = 98
        self.type = "Range"

    
