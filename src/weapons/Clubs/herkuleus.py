from src.weapons.weapon import Weapon


class Herkuleus(Weapon):
    def __init__(self):
        self.name = "Herkuleus"
        self.damage = 60
        self.accuracy = 85
        self.type = "Melee"

