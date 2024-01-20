from src.weapons.weapon import Weapon

class DemonicBow(Weapon):
    def __init__(self):
        self.name = "Demonic bow"
        self.damage = 36
        self.accuracy = 90
        self.type = "Range"

    
