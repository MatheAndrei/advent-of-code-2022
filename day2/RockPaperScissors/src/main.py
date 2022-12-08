from src.entities.round import Round


rounds = list()


def load_strategy_guide(file_path):
    with open(file_path, 'r') as fd:
        lines = fd.readlines()
        for line in lines:
            line_elems = line.split()
            attack = line_elems[0]
            counter_attack = line_elems[1]
            round = Round(attack, counter_attack)
            rounds.append(round)


def solve_one() -> int:
    total_score = sum(map(lambda round: round.score, rounds))
    return total_score


def solve_two() -> int:
    total_score = sum(map(lambda round: round.response, rounds))
    return total_score


def main():
    file_path = 'data/strategy_guide.txt'
    load_strategy_guide(file_path)
    print(f"Rounds: {rounds}")

    # PART ONE
    # What would your total score be if everything goes exactly according to your strategy guide?
    total_score = solve_one()
    print(f"Total score according to strategy guide (PART ONE): {total_score}")

    # PART TWO
    # Following the Elf's instructions for the second column,
    # what would your total score be if everything goes exactly according to your strategy guide?
    total_score = solve_two()
    print(f"Total score according to strategy guide (PART TWO): {total_score}")


if __name__ == '__main__':
    main()