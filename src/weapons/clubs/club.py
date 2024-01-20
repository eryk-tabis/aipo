from src.weapons.weapon import Weapon


class Club(Weapon):
    def __init__(self):
        self.name = "Club"
        self.damage = 15
        self.accuracy = 60
        self.type = "Melee"

