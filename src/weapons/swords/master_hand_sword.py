from src.weapons.weapon import Weapon
class KnightHandSword(Weapon):
    def __init__(self):
        self.name = "Knight handed sword"
        self.damage = 28
        self.accuracy = 90
        self.type = "Melee"

