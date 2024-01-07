from src.races.race import Race
from src.weapons.sword import Sword
class Human(Race):
    def __init__(self):
        super(Human, self).__init__()
        self.hp = 100
        self.equipped = Sword()
