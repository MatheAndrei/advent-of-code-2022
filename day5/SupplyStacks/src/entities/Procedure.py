from src.entities.Stack import Stack


class Procedure:
    def __init__(self, no_crates: int, src_stack: Stack, dst_stack: Stack):
        self.__no_crates: int = no_crates
        self.__src_stack: Stack = src_stack
        self.__dst_stack: Stack = dst_stack

    def execute_9000(self):
        for step in range(self.__no_crates):
            crate = self.__src_stack.pop()
            self.__dst_stack.push(crate)

    def execute_9001(self):
        crates: list[str, ...] = list()
        for step in range(self.__no_crates):
            crate = self.__src_stack.pop()
            crates.append(crate)
        for crate in reversed(crates):
            self.__dst_stack.push(crate)

    def __str__(self):
        return f"move {self.__no_crates} from {self.__src_stack.id} to {self.__dst_stack.id}"

    def __repr__(self):
        return str(self)
