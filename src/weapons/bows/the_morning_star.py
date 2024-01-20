from src.weapons.weapon import Weapon

class TheMorningStar(Weapon):
    def __init__(self):
        self.name = "The Morning Star"
        self.damage = 40
        self.accuracy = 110
        self.type = "Range"

    
