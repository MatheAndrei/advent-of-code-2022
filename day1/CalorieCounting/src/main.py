from pprint import pprint

from src.entities.elf import Elf
from src.entities.item import Item


elves = dict()


def load_inventories(file_path):
    with open(file_path, 'r') as fd:
        line = fd.readline()
        while line:
            elf = Elf()
            elves[id(elf)] = elf
            while not line.isspace() and line:
                calories = int(line)
                item = Item(calories)
                elf.add_item(item)
                line = fd.readline()
            line = fd.readline()


def solve_one() -> Elf:
    richest_elf: Elf = max(elves.values(), key=lambda elf: elf.total_calories)
    return richest_elf


def solve_two() -> tuple[int, list[Elf]]:
    elves_sorted = sorted(elves.values(), key=lambda elf: elf.total_calories, reverse=True)
    top_three_elves = elves_sorted[:3]
    total_calories = sum(map(lambda elf: elf.total_calories, top_three_elves))
    return total_calories, top_three_elves


def main():
    file_path = "data/inventory.txt"
    load_inventories(file_path)
    pprint(elves, indent=4)

    # PART ONE
    # Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    richest_elf = solve_one()
    print(f"Richest elf: {richest_elf}")
    print(f"Result: {richest_elf.total_calories}")

    # PART TWO
    # Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
    total_calories, top_three_elves = solve_two()
    print(f"Top 3 elves with a total of {total_calories} calories: {top_three_elves}")


if __name__ == '__main__':
    main()
