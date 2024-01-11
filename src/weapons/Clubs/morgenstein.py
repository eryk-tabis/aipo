from src.weapons.weapon import Weapon


class Morgenstein(Weapon):
    def __init__(self):
        self.name = "Morgenstein"
        self.damage = 32
        self.accuracy = 72
        self.type = "Melee"

