from src.weapons.weapon import Weapon


class SpikeClub(Weapon):
    def __init__(self):
        self.name = "Spike Club"
        self.damage = 18
        self.accuracy = 60
        self.type = "Melee"

