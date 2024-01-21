from src.locations.location import Location
from typing import Union


class World:
    current_location: Union[Location, None]
    def __init__(self):
        self.current_location= None
        self.locations = {}

    def get_current_location(self):
        return self.current_location

    def set_current_location(self, location):
        self.current_location = location
