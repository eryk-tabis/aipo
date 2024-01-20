from src.weapons.weapon import Weapon

class Battlebow(Weapon):
    def __init__(self):
        self.name = "Battle bow"
        self.damage = 12
        self.accuracy = 84
        self.type = "Range"

    
