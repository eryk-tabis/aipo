colors = {
    "red": "\33[91m",
    "green": "\33[92m",
    "yellow":  "\33[93m",
    "orange": "\33[94m",
    "end": "\033[0m",
}

class Colorizer():
    @staticmethod
    def colorize_green(text):
        return f"{colors['green']}{text}{colors['end']}"
    def colorize_red(text):
        return f"{colors['red']}{text}{colors['end']}"
    def colorize_orange(text):
        return f"{colors['orange']}{text}{colors['end']}"

