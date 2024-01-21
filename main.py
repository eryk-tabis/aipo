from src.characters import player
from inventory import inventory
from setup_world import setup_world
from src.characters.player import create_player
from src.characters.warrior import Warrior
from src.characters.shooter import Shooter
from src.characters.tank import Tank
from fight import fight
from src.items.item import Item
from src.locations.world import World

class_dict = {"czlowiek": Warrior, "ork": Tank, "elf":Shooter}

lady_of_lake_flag = False

def main():
    print(get_dialogs_from_file("opening.txt"))
    while True:
        class_choice = input(get_dialogs_from_file("class_choice.txt"))
        if class_choice.lower() == "czlowiek" or class_choice.lower() == "ork" or class_choice.lower() == "elf":
            break
        else:
            print("Niepoprawna klasa")
    name_choice = input(get_dialogs_from_file("name_choice.txt"))
    player = create_character(class_choice, name_choice)
    world = World()
    setup_world(world)
    print("Ta noc była dziwna dla Ciebie " + name_choice + get_dialogs_from_file("opening_2.txt"))
    print(get_dialogs_from_file("opening_3.txt"))
    print(get_dialogs_from_file("opening_4.txt"))
    while True:
        if (world.current_location.get_cutsceneses()):
            for cutscene in world.current_location.get_cutsceneses():
                cutscene.play_cutscene()
                world.current_location.remove_cutscene(cutscene)
        if (world.current_location.get_enemies()):
            for enemy in world.current_location.get_enemies():
                if enemy.name == "Pani jeziora":
                    print("Spotykasz potężną Panią jeziora, która bez słowa Cię atakuje!!!")
                wasEnemyDefeated = fight(player, enemy)
                if not wasEnemyDefeated: return
                if enemy.name == "Pani jeziora":
                    print(get_dialogs_from_file("lady_of_the_lake_1.txt")
                          + player.name
                          + get_dialogs_from_file("lady_of_the_lake_2.txt"))
                    lady_of_lake_flag = True
                    # TODO: Add crucial item
                    # player.add_to_inventory(item)
                if enemy.name == "Sventino":
                    print(get_dialogs_from_file("sventino_2.txt"))
                    print("Koniec gry")
                    input()  # just to pause the program
                    return
                world.current_location.remove_enemy(enemy)
        print("Jesteś w: " + world.current_location.name)
        print("Co chcesz zrobić?")
        print(" - Sprawdź ekwipunek (inv)"
              "\n - Idź do innej lokacji (move)")
        action = str(input()).lower()
        if action == "sprawdź ekwipunek" or action == "inv":
            inventory(player)
        elif action == "idź do innej lokacji" or action == "move":
            play_location(world, lady_of_lake_flag)
        else:
            print("Niepoprawna akcja")


def play_location(world: World, lady_of_lake_flag):
    """Play the location"""
    print(world.current_location.get_description())
    print(world.current_location.get_locations_nearby(lady_of_lake_flag))
    world.current_location = world.current_location.get_location(input("Gdzie chcesz iść?"))


def create_character(class_choice, name_choice):
    """Create the character"""
    player = create_player(name_choice, class_dict[class_choice])
    item = Item("Healing Potion", "Heals 10 Hp", "Healing", 10, 1)
    player.add_to_inventory(item)
    return player


def get_dialogs_from_file(file_name):
    """Get the dialogs from a file"""
    string = ""
    with open("src/dialogs/" + file_name, "r", encoding="utf-8") as file:
        string += file.read()
    return string


if __name__ == "__main__":
    main()
