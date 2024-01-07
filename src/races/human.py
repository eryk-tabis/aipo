from src.races.race import Race
from src.weapons.sword import Sword
class Human(Race):
    hp = 100
    equipped = Sword()
    def __init__(self):
        super().__init__()