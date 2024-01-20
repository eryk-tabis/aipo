from src.weapons.weapon import Weapon


class WarHammer(Weapon):
    def __init__(self):
        self.name = "War hammer"
        self.damage = 40
        self.accuracy = 80
        self.type = "Melee"

