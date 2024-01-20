from src.weapons.weapon import Weapon


class TheGiantStaff(Weapon):
    def __init__(self):
        self.name = "The giant staff"
        self.damage = 30
        self.accuracy = 80
        self.type = "Melee"

