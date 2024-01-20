from src.cutscenes.cutscene import Cutscene
class ManasztorConventCutscene(Cutscene):
    def __init__(self):
        super().__init__()
    def play_cutscene(self):
        print(self.get_dialogs_from_file("manasztor_convent.txt"))
