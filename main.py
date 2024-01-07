from src.locations.world import World
from src.locations.location import Location
from setup_world import setup_world
from fight import fight
from inventory import inventory
from src.characters.player import create_player
from src.characters.warrior import Warrior
from src.races.human import Human
from src.items.item import Item



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
                fight(player, enemy)
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
    player = create_player("Player", Warrior, Human)("Player")
    print(player.hp)
    item = Item("Healing Potion", "Heals 10 Hp", "Healing", 10, 1)
    player.add_to_inventory(item)
    return player


if __name__ == "__main__":
    main()
