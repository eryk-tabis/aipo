from random import randint
from src.characters.character import Character

class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.hp = 0
        self.damage = 0
        self.defense = 0
        self.agility = 0

    def receive_damage(self, damage: int):
        difference = (damage - self.defense)
        self.hp -= difference if difference >= 0 else 0
    def try_to_attack(self):
        return randint(0, 100) < self.agility
    def get_damage(self):
        return self.damage
    



