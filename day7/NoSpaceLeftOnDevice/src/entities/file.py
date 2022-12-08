from src.entities.directory import Directory


class File:
    def __init__(self, parent: Directory, name: str, size: int):
        self.__parent = parent
        self.__name = name
        self.__size = size
        self.__level = parent.level + 1

    @property
    def parent(self) -> Directory:
        return self.__parent

    @property
    def name(self) -> str:
        return self.__name

    @property
    def size(self) -> int:
        return self.__size

    @property
    def level(self) -> int:
        return self.__level

    def __str__(self):
        return '\t' * self.__level + '- ' + str(self.__name) + ' (file, size=' + str(self.__size) + ')'
