from __future__ import annotations


class Directory:
    def __init__(self, parent: Directory, name: str):
        self.__parent = parent
        self.__name = name
        self.__content = []
        if parent is None:
            self.__level = 0
        else:
            self.__level = parent.level + 1

    @property
    def parent(self) -> Directory:
        return self.__parent

    @property
    def name(self) -> str:
        return self.__name

    @property
    def size(self):
        size = 0
        for entry in self.__content:
            size += entry.size
        return size

    @property
    def contents(self) -> list:
        return self.__content

    @property
    def level(self) -> int:
        return self.__level

    def add_entry(self, entry):
        self.__content.append(entry)

    def find_directory(self, name: str) -> Directory:
        for entry in self.__content:
            if isinstance(entry, Directory) and entry.name == name:
                return entry

    def __str__(self):
        string = ""
        string += '\t' * self.__level + '- ' + str(self.__name) + ' (dir)\n'
        for file in self.__content:
            string += str(file) + '\n'
        string = string[:-1]
        return string
