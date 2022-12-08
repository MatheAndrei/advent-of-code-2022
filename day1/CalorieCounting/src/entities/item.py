class Item:
    def __init__(self, calories: int):
        self.__calories: int = calories

    @property
    def calories(self) -> int:
        return self.__calories

    def __str__(self):
        return str(self.__calories)

    def __repr__(self):
        return str(self)