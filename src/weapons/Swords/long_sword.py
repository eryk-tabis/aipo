from src.weapons.weapon import Weapon
class LongSword(Weapon):
    def __init__(self):
        self.name = "Long sword"
        self.damage = 20
        self.accuracy = 76
        self.type = "Melee"

