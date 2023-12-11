def create_player(name: str, character_class: object, race_class: object):
    class Player(character_class, race_class):
        def __init__(self, name: str):
            super().__init__()
            self.name = name
    return Player
