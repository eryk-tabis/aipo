from random import randint
from colorizer import Colorizer
from src.characters.character import Character
from src.characters.warrior import Warrior
from inventory import inventory

def execute_enemy_attack(player, enemy):
     if(player.hp == 0 or enemy.hp == 0): return
     wasAttackBlocked = randint(0, 30) == 1
     if(wasAttackBlocked):
         print(f"Enemy attacked you with {Colorizer.colorize_orange(enemy.equipped.name)} {Colorizer.colorize_green('but you blocked the attack')}. You have {Colorizer.colorize_green(player.hp)} hp left")
         return
     
     player.hp = (player.hp - enemy.equipped.damage)
     print(f"Enemy successfuly attacked you with {enemy.equipped.name} and you have {Colorizer.colorize_green(player.hp)} hp left")

def execute_player_attack(player, enemy):
    if(player.hp == 0 or enemy.hp == 0): return
    wasAttackBlocked = randint(0, 8) == 1
    if wasAttackBlocked:
        print(f"You attack the {Colorizer.colorize_red(enemy.name)} with {Colorizer.colorize_orange(player.equipped.name)} but {Colorizer.colorize_red('the enemy blocked your attack')}. It has {Colorizer.colorize_red(enemy.hp)} hp left")
        return
    
    enemy.hp -= player.equipped.damage
    print(f"You attack the {Colorizer.colorize_red(enemy.name)} with {Colorizer.colorize_orange(player.equipped.name)}. It has {Colorizer.colorize_red(enemy.hp)} hp left")

def loot_enemy_iventory(player, enemy: Character):
    print(f"You have recieved some items from the defeated enemy:")
    for item in enemy.inventory.keys():
        player.add_to_inventory(enemy.inventory[item]["item"])
        print(Colorizer.colorize_orange(f" - {enemy.inventory[item]['amount']}x {enemy.inventory[item]['item'].name}"))

def fight(player, enemy: Warrior):
    """Fight the enemy"""
    print(f"You encounter an {Colorizer.colorize_red(enemy.name)}")
    while enemy.hp > 0 and player.hp > 0:
        print(f"It is your turn, you have {Colorizer.colorize_green(player.hp)} hp and the enemy has {Colorizer.colorize_red(enemy.hp)} hp, what do you want to do?")
        print(f"\n - Attack (a)"
              f"\n - Open inventory (inv) \n")
        action = input().lower()
        if action == "attack" or action == "a":
            execute_player_attack(player, enemy)
            execute_enemy_attack(player, enemy)
        elif action == "open inventory" or action == "inv":
            inventory(player)
        else:
            print(f"")
            execute_enemy_attack(player, enemy)
    if(enemy.hp == 0):
        print(f"You have defeated {enemy.name}! Congrats!")
        isInventoryNotEmpty = len(enemy.inventory.keys()) > 0
        if(isInventoryNotEmpty):
            loot_enemy_iventory(player, enemy)
        return True
    if(player.hp == 0):
        print(f"You have been defeated by {enemy.name} :(")
        return False
       