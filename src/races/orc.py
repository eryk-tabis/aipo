from src.races.race import Race
from src.weapons.clubs.club import Club



class Orc(Race):
    def __init__(self):
        super(Orc, self).__init__()
        self.hp = 120
        self.stamina = 80
        self.damage = 15
        self.defense = 15
        self.agility = 60
        self.luck = 5
        self.equipped = Club()