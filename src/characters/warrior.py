from src.characters.character import Character
from src.races.human import Human
class Warrior(Character,Human):
    def __init__(self):
        super().__init__()