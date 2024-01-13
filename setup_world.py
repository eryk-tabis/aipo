from src.items.item import Item
from src.characters.warrior import Warrior
from src.locations.world import World
from src.locations.location import Location
def setup_world(obj: World):
    """Setup the world with locations and items"""
    start_location = Location()
    start_location.name = "Start"
    start_location.description = "You are at the start"
    obj.set_current_location(start_location)
    second_location = Location()
    second_location.name = "North"
    second_location.description = "You are at the north location"
    start_location.add_location(second_location, "north")
    second_location.add_location(start_location, "start")
    """Mock enemies"""
    enemy1 = Warrior()
    enemy1.name = "Bob"
    item = Item("Healing Potion", "Heals 10 Hp", "Healing", 10, 1)
    enemy1.inventory.update({item.name: {"item": item, "amount": item.amount}})
    second_location.add_enemy(enemy1)
    """End of Mock enemies"""
    return obj
