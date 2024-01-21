from src.races.race import Race
from src.weapons.swords.sword import Sword
class Human(Race):
    def __init__(self):
        super(Human, self).__init__()
        self.hp = 100
        self.stamina = 100
        self.strength = 10
        self.defense = 10
        self.agility = 75
        self.luck = 10
        self.equipped = Sword()
