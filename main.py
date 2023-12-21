from src.locations.world import World
from src.locations.location import Location
from setup_world import setup_world
from fight import fight



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
        "What about items?"
        play_location(world)


def play_location(world: World):
    """Play the location"""
    print(world.current_location.get_description())
    print(world.current_location.get_locations_nearby())
    world.current_location = world.current_location.get_location(input("Where do you want to go?"))


def create_character():
    """Create the player character"""
    pass

def open_player_inventory(player):
    """Check the player inventory"""
    promt = "You have this items in your inventory:"
    for item in player.inventory:
        promt += f"\n - {item.name}"
    print(promt)
    
    pass

if __name__ == "__main__":
    main()
