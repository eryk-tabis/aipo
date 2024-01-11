from src.weapons.weapon import Weapon


class TreeTrunk(Weapon):
    def __init__(self):
        self.name = "Tree trunk"
        self.damage = 50
        self.accuracy = 75
        self.type = "Melee"

