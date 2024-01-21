from src.races.race import Race
from src.weapons.bows.bow import Bow
class Elf(Race):
    def __init__(self):
        super(Elf,self).__init__()
        self.hp = 80
        self.stamina = 120
        self.damage = 5
        self.defense = 5
        self.agility = 90
        self.luck = 15
        self.equipped = Bow()

