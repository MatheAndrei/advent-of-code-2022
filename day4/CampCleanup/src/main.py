import pprint

from src.entities.Assignment import Assignment

assignment_pairs: list[tuple[Assignment, Assignment]] = list()


def load_assignment_pair(file_path):
    with open(file_path, 'r') as fd:
        lines = fd.readlines()
        for line in lines:
            line_elems = line.split(',')
            assignment1 = line_elems[0].split('-')
            assignment2 = line_elems[1].split('-')
            elf1_assignment = Assignment(int(assignment1[0]), int(assignment1[1]))
            elf2_assignment = Assignment(int(assignment2[0]), int(assignment2[1]))
            assignment_pairs.append((elf1_assignment, elf2_assignment))


def solve_one() -> int:
    no_pairs = 0
    for pair in assignment_pairs:
        assignment1 = pair[0]
        assignment2 = pair[1]
        if (assignment1.start_section >= assignment2.start_section and assignment1.end_section <= assignment2.end_section) or \
                (assignment1.start_section <= assignment2.start_section and assignment1.end_section >= assignment2.end_section):
            no_pairs += 1
    return no_pairs


def solve_two() -> int:
    no_pairs = 0
    for pair in assignment_pairs:
        assignment1 = pair[0]
        assignment2 = pair[1]
        range1 = set(range(assignment1.start_section, assignment1.end_section + 1))
        range2 = set(range(assignment2.start_section, assignment2.end_section + 1))
        overlap = range1 & range2
        if len(overlap) != 0:
            no_pairs += 1
    return no_pairs


def main():
    file_path = 'data/assignment_pairs.txt'
    load_assignment_pair(file_path)

    # PART ONE
    # In how many assignment pairs does one range fully contain the other?
    no_pairs = solve_one()
    print(f"Number of assignment pair (PART ONE): {no_pairs}")

    # PART TWO
    # In how many assignment pairs do the ranges overlap?
    no_pairs = solve_two()
    print(f"Number of assignment pair (PART TWO): {no_pairs}")



if __name__ == '__main__':
    main()
