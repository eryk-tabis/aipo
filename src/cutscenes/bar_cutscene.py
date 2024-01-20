from src.cutscenes.cutscene import Cutscene
class BarCutscene(Cutscene):
    def __init__(self):
        super().__init__()
    def play_cutscene(self):
        print(self.get_dialogs_from_file("bar.txt"))
