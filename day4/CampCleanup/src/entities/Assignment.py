class Assignment:
    def __init__(self, start_section: int, end_section: int):
        self.__start_section: int = start_section
        self.__end_section: int = end_section

    @property
    def start_section(self) -> int:
        return self.__start_section

    @property
    def end_section(self) -> int:
        return self.__end_section

    def __str__(self):
        return f"{self.__start_section}-{self.__end_section}"

    def __repr__(self):
        return str(self)
