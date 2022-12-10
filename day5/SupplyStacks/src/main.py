from src.entities.Procedure import Procedure
from src.entities.Stack import Stack

stacks: list[Stack, ...] = list()
procedures: list[Procedure, ...] = list()


def load_stacks_procedures(file_path):
    with open(file_path, 'r') as fd:
        layers: list[str, ...] = []

        while True:
            line = fd.readline()
            if line == "":
                break
            line = line.rstrip()

            if '[' in line:
                layers.insert(0, line)
            elif ' 1' == line[:2]:
                # for each layer add the crates to the corresponding stack
                for layer in layers:
                    stack_num = 1
                    # go through each crate
                    while layer != '':
                        crate = layer[0:4]
                        symbol = crate[1]
                        # check if current stack has a crate on this layer
                        if symbol != ' ':
                            if stack_num > len(stacks):
                                stack = Stack(stack_num)
                                stack.push(symbol)
                                stacks.append(stack)
                            else:
                                stacks[stack_num - 1].push(symbol)
                        layer = layer[4:]
                        stack_num += 1
            elif 'move' in line:
                # get numbers from procedure
                numbers = [int(token) for token in line.split() if token.isdigit()]

                no_crates = numbers[0]
                src_stack_num = numbers[1]
                src_stack = stacks[src_stack_num - 1]
                dst_stack_num = numbers[2]
                dst_stack = stacks[dst_stack_num - 1]

                procedure = Procedure(no_crates, src_stack, dst_stack)
                procedures.append(procedure)


def solve_one() -> str:
    for procedure in procedures:
        procedure.execute_9000()
    result = ''.join(map(lambda stack: stack.top(), stacks))
    return result


def solve_two() -> str:
    for procedure in procedures:
        procedure.execute_9001()
    result = ''.join(map(lambda stack: stack.top(), stacks))
    return result


def main():
    file_path = 'data/stacks_procedures.txt'
    load_stacks_procedures(file_path)

    # PART ONE
    # After the rearrangement procedure completes, what crate ends up on top of each stack?
    # result = solve_one()
    # print(f"Crates on top of each stack (PART ONE): {result}")

    # !!! Only one solve function can be called and the other one commented,
    # !!! because it modifies the stacks and procedures

    # PART TWO
    # After the rearrangement procedure completes, what crate ends up on top of each stack?
    result = solve_two()
    print(f"Crates on top of each stack (PART TWO): {result}")


if __name__ == '__main__':
    main()
