from pprint import pformat


from src.entities.item import Item


class Elf:
    def __init__(self):
        self.__total_calories: int = 0
        self.__inventory: list[Item] = list()

    @property
    def total_calories(self) -> int:
        return self.__total_calories

    @property
    def inventory(self) -> list[Item]:
        return self.__inventory

    def add_item(self, item: Item):
        self.__total_calories += item.calories
        self.__inventory.append(item)

    def __str__(self):
        return str({
            'total_calories': self.__total_calories,
            'items': self.__inventory
        })

    def __repr__(self):
        return str(self)