from src.weapons.weapon import Weapon


class BigClub(Weapon):
    def __init__(self):
        self.name = "Big club"
        self.damage = 25
        self.accuracy = 55
        self.type = "Melee"

