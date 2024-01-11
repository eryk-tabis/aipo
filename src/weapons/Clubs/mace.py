from src.weapons.weapon import Weapon


class Mace(Weapon):
    def __init__(self):
        self.name = "Mace"
        self.damage = 20
        self.accuracy = 65
        self.type = "Melee"

