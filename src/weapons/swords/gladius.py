from src.weapons.weapon import Weapon
class Gladius(Weapon):
    def __init__(self):
        self.name = "Gladius"
        self.damage = 14
        self.accuracy = 92
        self.type = "Melee"

