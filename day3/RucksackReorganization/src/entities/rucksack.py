class Rucksack:
    def __init__(self, content: str):
        self.__length: int = len(content)
        self.__content: str = content
        self.__first_compartment: list[str] = [*content][:self.__length // 2]
        self.__second_compartment: list[str] = [*content][self.__length // 2:]

    @property
    def content(self) -> str:
        return self.__content

    @property
    def first_compartment(self) -> list[str]:
        return self.__first_compartment

    @property
    def second_compartment(self) -> list[str]:
        return self.__second_compartment

    @property
    def error(self) -> str:
        return (set(self.__first_compartment) & set(self.__second_compartment)).pop()

    def __str__(self):
        return str({
            'error': self.error,
            'first_compartment': self.__content[:self.__length // 2],
            'second_compartment': self.__content[self.__length // 2:]
        })

    def __repr__(self):
        return str(self)
