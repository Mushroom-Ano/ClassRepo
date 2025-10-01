from person import *

class Graduate(Person):


    def __init__(self, scheme, location, first_name: str, last_name: str, age: int):
        super().__init__(first_name, last_name, age)
        self._scheme = scheme
        self.__location = location

    @property
    def location(self) -> str:
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location
        

student = Graduate("Software Engineer", "Leeds", "John", "Doe", 25)

print(student.first_name)