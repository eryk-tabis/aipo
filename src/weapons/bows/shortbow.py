from src.weapons.weapon import Weapon

class Shortbow(Weapon):
    def __init__(self):
        self.name = "Short bow"
        self.damage = 16
        self.accuracy = 90
        self.type = "Range"

    
