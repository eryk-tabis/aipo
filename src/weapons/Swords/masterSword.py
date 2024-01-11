from src.weapons.weapon import Weapon
class MasterSword(Weapon):
    def __init__(self):
        self.name = "Master Sword"
        self.damage = 24
        self.accuracy = 84
        self.type = "Melee"

