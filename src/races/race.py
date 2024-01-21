from random import randint


class Race():
    def __init__(self):
        self.hp = 0
        self.stamina = 0
        self.strength = 0
        self.defense = 0
        self.agility = 0
        self.luck = 0
        self.equipped = None

    def receive_damage(self, damage: int):
        self.hp -= (damage - self.defense)
    def try_to_attack(self):
        return randint(0, 100) < self.agility
