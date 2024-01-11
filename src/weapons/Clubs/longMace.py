from src.weapons.weapon import Weapon


class LongClub(Weapon):
    def __init__(self):
        self.name = "Long mace"
        self.damage = 25
        self.accuracy = 70
        self.type = "Melee"

