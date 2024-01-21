from src.characters.character import Character
from src.races.orc import Orc
class Tank(Character,Orc):
    def __init__(self):
        super(Orc, self).__init__()
