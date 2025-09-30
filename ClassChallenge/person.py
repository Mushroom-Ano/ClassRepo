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






