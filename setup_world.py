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
    return obj
