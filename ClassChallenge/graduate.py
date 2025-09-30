from person import *

class Graduate:

    def __init__(self, person: Person, scheme, location):
        self.person = person
        self._scheme = scheme
        self.__location = location

    @property
    def location(self) -> str:
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location
        
