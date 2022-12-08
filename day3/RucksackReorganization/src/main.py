from src.entities.rucksack import Rucksack

rucksacks = list()


def priority(item: str) -> int:
    return ord(item) - ord('a') + 1 if 'a' <= item <= 'z' else 26 + ord(item) - ord('A') + 1


def load_rucksacks(file_path):
    with open(file_path, 'r') as fd:
        lines = fd.readlines()
        for line in lines:
            rucksack = Rucksack(line.rsplit()[0])
            rucksacks.append(rucksack)


def solve_one() -> int:
    sum_priorities = sum(map(lambda rucksack: priority(rucksack.error), rucksacks))
    return sum_priorities


def solve_two() -> int:
    groups = list()
    badges = list()

    # divide in groups of three
    group_num = 0
    while group_num * 3 + 2 < len(rucksacks):
        group = [rucksacks[group_num * 3 + 0], rucksacks[group_num * 3 + 1], rucksacks[group_num * 3 + 2]]
        groups.append(group)
        group_num += 1

    # get badges of each group
    for group in groups:
        first_content = [*group[0].content]
        second_content = [*group[1].content]
        third_content = [*group[2].content]
        badge = (set(first_content) & set(second_content) & set(third_content)).pop()
        badges.append(badge)

    # sum all priorities of the badges
    sum_priorities = sum(map(lambda badge: priority(badge), badges))

    return sum_priorities


def main():
    file_path = 'data/rucksacks.txt'
    load_rucksacks(file_path)
    print(f"Rucksacks: {rucksacks}")

    # PART ONE
    # Find the item type that appears in both compartments of each rucksack.
    # What is the sum of the priorities of those item types?
    sum_priorities = solve_one()
    print(f"Sum of the priorities of errors: {sum_priorities}")

    # PART TWO
    # Find the item type that corresponds to the badges of each three-Elf group.
    # What is the sum of the priorities of those item types?
    sum_priorities = solve_two()
    print(f"Sum of the priorities of badges: {sum_priorities}")


if __name__ == '__main__':
    main()
