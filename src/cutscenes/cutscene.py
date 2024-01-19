class Cutscene:
    def __init__(self):
        pass

    def play_cutscene(self):
        pass
    @staticmethod
    def get_dialogs_from_file(file_name):
        string = ""
        with open("src/dialogs/" + file_name, "r", encoding="utf-8") as file:
            string += file.read()
        return string
