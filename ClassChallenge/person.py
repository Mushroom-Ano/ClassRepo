from exception import Error

class Person:

    """
        Defines a person with getters and setters
    """

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self._last_name = last_name
        self.__age = age

    def get_last_name(self) -> str:
        return self._last_name

    def set_last_name(self, name):
        self._last_name = name

    def get_age(self) -> int:
        return self.__age
    
    def set_age(self, age):
        if self.__age > 0:
            print("Age cannot be negative")
            raise Error("Age cannot be negative")
        self.__age = age













