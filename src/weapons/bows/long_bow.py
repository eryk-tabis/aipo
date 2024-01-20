from src.weapons.weapon import Weapon

class Longbow(Weapon):
    def __init__(self):
        self.name = "Long bow"
        self.damage = 20
        self.accuracy = 80
        self.type = "Range"

    
