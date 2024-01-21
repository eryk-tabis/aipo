from random import randint


class Race():
    def __init__(self):
        self.hp = 0
        self.stamina = 0
        self.damage = 0
        self.defense = 0
        self.agility = 0
        self.luck = 0
        self.equipped = None
    
    def receive_damage(self, damage: int):
        difference = (damage - self.defense)
        self.hp -= difference if difference >= 0 else 0
    def try_to_attack(self):
        return randint(0, 100) < self.agility
    def get_damage(self):
        return self.equipped.damage if self.equipped else self.damage
