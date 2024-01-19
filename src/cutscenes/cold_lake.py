from src.cutscenes.cutscene import Cutscene
from fight import fight
class MichelHouseCutscene(Cutscene):
    def __init__(self):
        super().__init__()
    def play_cutscene(self, world, player):
        print("Spotykasz potężną Panią jeziora, która bez słowa Cię atakuje!!!")

        print(self.get_dialogs_from_file("michel_house_cutscene.txt"))