from src.characters.character import Character
from src.races.elf import Elf
class Shooter(Character,Elf):
    def __init__(self):
        super(Shooter, self).__init__()
