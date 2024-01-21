from src.weapons.weapon import Weapon
class Sword(Weapon):
    def __init__(self):
        self.name = "Sword"
        self.damage = 25
        self.accuracy = 80
        self.type = "Melee"

