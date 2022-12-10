class Stack:
    def __init__(self, id):
        self.__id: int = id
        self.__data: list[str, ...] = list()

    @property
    def id(self) -> int:
        return self.__id

    def push(self, crate: str):
        self.__data.append(crate)

    def pop(self) -> str:
        return self.__data.pop()

    def top(self) -> str:
        return self.__data[-1]

    def __str__(self):
        return str({'id': self.__id, 'data': self.__data})

    def __repr__(self):
        return str(self)
