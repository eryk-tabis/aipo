from src.weapons.weapon import Weapon
class ShortSword(Weapon):
    def __init__(self):
        self.name = "Short sword"
        self.damage = 8
        self.accuracy = 90
        self.type = "Melee"

