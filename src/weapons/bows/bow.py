from src.weapons.weapon import Weapon

class Bow(Weapon):
    def __init__(self):
        self.name = "Bow"
        self.damage = 20
        self.accuracy = 80
        self.type = "Range"

    
