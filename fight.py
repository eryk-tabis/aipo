from random import randint
from colorizer import Colorizer
from src.enemies.enemy import Enemy
from src.characters.character import Character
from src.characters.warrior import Warrior
from inventory import inventory


def execute_attack(attacker, attacked):
    if(attacker.hp <= 0 or attacked.hp <= 0): return
    wasAttackSuccessfull = attacker.try_to_attack()
    if wasAttackSuccessfull:
        attacked.receive_damage(attacker.get_damage())
    return wasAttackSuccessfull

def execute_enemy_attack(player, enemy: Enemy):
     wasAttackSuccessfull = execute_attack(enemy, player)
     if(wasAttackSuccessfull == None): return
     if(not wasAttackSuccessfull):
         print(f"Przeciwnik zaatakował Ciebię {Colorizer.colorize_green('ale nie trafił!')}. Pozostało Ci {Colorizer.colorize_green(player.hp)} hp")
         return
     
     if(player.hp <= 0): return
     print(f"Przeciwnik zaatakował Cię i zostało Ci {Colorizer.colorize_green(player.hp)} hp")

def execute_player_attack(player, enemy: Enemy):
    wasAttackSuccessfull = execute_attack(player, enemy)
    if wasAttackSuccessfull == None: return
    if not wasAttackSuccessfull:
        print(f"Zaatakowałeś {Colorizer.colorize_red(enemy.name)} za pomocą {Colorizer.colorize_orange(player.equipped.name)} ale {Colorizer.colorize_red('nie trafiłeś!')}. Przeciwnik ma {Colorizer.colorize_red(enemy.hp)} hp")
        return
    
    if(enemy.hp <= 0): return
    print(f"Zaatakowałeś {Colorizer.colorize_red(enemy.name)} za pomocą {Colorizer.colorize_orange(player.equipped.name)}. Przewnik ma {Colorizer.colorize_red(enemy.hp)} hp")

def loot_enemy_iventory(player, enemy: Enemy):
    print(f"Otrzymałeś następujące rzeczy od przeciwnika:")
    for item in enemy.inventory.keys():
        player.add_to_inventory(enemy.inventory[item]["item"])
        print(Colorizer.colorize_orange(f" - {enemy.inventory[item]['item'].name} (x{enemy.inventory[item]['amount']})"))

def fight(player, enemy: Enemy):
    """Fight the enemy"""
    print(f"Walczysz o życie z {Colorizer.colorize_red(enemy.name)}")
    print(enemy.agility, player.agility)
    if(enemy.agility > player.agility):
        execute_enemy_attack(player, enemy)
    while enemy.hp > 0 and player.hp > 0:
        print(f"Twoja kolej, masz {Colorizer.colorize_green(player.hp)} hp a przeciwnik {Colorizer.colorize_red(enemy.hp)} hp, co zamierzasz zrobić?")
        print(f"\n - Atakuj (a)"
              f"\n - Sprawdź ekwipunek (inv) \n")
        action = input().lower()
        if action == "atakuj" or action == "a":
            execute_player_attack(player, enemy)
            execute_enemy_attack(player, enemy)
        elif action == "otwórz ekwipunek" or action == "inv":
            inventory(player)
        else:
            print(f"")
            execute_enemy_attack(player, enemy)
    if(enemy.hp <= 0):
        
        print(f"Zabiłeś przeciwnika {Colorizer.colorize_red(enemy.name)}! Gratulacje!\n")
        isInventoryNotEmpty = len(enemy.inventory.keys()) > 0
        if(isInventoryNotEmpty):
            loot_enemy_iventory(player, enemy)
        return True
    if(player.hp <= 0):
        print(f"{Colorizer.colorize_red(enemy.name)} Cię zabił :(")
        return False
       