from src.characters import player
from inventory import inventory
from setup_world import setup_world
from src.characters.player import create_player
from src.characters.warrior import Warrior
from fight import fight
from src.items.item import Item
from src.locations.world import World


def main():
    world = World()
    setup_world(world)
    player = create_character()
    while True:
        if(world.current_location.get_cutsceneses()):
            for cutscene in world.current_location.get_cutsceneses():
                cutscene.play_cutscene()
        if(world.current_location.get_enemies()):
            for enemy in world.current_location.get_enemies():
                wasEnemyDefeated = fight(player, enemy)
                if not wasEnemyDefeated : return
        print("What do you want to do?")
        print(" - Inventory"
              "\n - Go to location")
        action = str(input())
        if action.lower() == "inventory":
            inventory(player)
        elif action.lower() == "go to location":
            play_location(world)
        else:
            print("That is not a valid action")


def play_location(world: World):
    """Play the location"""
    print(world.current_location.get_description())
    print(world.current_location.get_locations_nearby())
    world.current_location = world.current_location.get_location(input("Where do you want to go?"))


def create_character():
    """Create the character"""
    #Now this is mock, changed when we have a character creator
    player = create_player("Player", Warrior)
    item = Item("Healing Potion", "Heals 10 Hp", "Healing", 10, 1)
    player.add_to_inventory(item)
    return player


if __name__ == "__main__":
    main()
