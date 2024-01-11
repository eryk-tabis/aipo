from src.races.race import Race
from aipo.src.weapons.Swords.sword import Sword
class Human(Race):
    def __init__(self):
        super(Human, self).__init__()
        self.hitPoints = 100
        self.stamina = 100
        self.strength = 10
        self.defense = 10
        self.agility = 10
        self.luck = 10
        self.equipped = Sword()
