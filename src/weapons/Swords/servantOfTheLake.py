from src.weapons.weapon import Weapon
class ServantOfTheLake(Weapon):
    def __init__(self):
        self.name = "Servant of the lake"
        self.damage = 42
        self.accuracy = 80
        self.type = "Melee"

