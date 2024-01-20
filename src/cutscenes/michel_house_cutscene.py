from src.cutscenes.cutscene import Cutscene
class MichelHouseCutscene(Cutscene):
    def __init__(self):
        super().__init__()
    def play_cutscene(self):
        print(self.get_dialogs_from_file("michel_house_cutscene.txt"))
