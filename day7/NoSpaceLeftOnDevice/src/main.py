import pprint

from src.entities.file import File
from src.entities.directory import Directory


def load_filesystem(file_path: str) -> Directory:
    root_dir: Directory = None
    current_dir: Directory = None

    with open(file_path, 'r') as fd:
        line = fd.readline()
        while line:
            line_elems = line.split()
            command = line_elems[1]

            match command:
                case 'cd':
                    if current_dir is None:
                        root_dir = Directory(None, '/')
                        current_dir = root_dir
                    else:
                        arg = line_elems[2]
                        if arg == '..':
                            current_dir = current_dir.parent
                        else:
                            current_dir = current_dir.find_directory(arg)
                    line = fd.readline()
                case 'ls':
                    line = fd.readline()
                    while True:
                        if line == "":
                            break
                        line_elems = line.split()
                        if line_elems[0] == 'dir':
                            name = line_elems[1]
                            current_dir.add_entry(Directory(current_dir, name))
                        elif line_elems[0].isdigit():
                            name = line_elems[1]
                            size = int(line_elems[0])
                            current_dir.add_entry(File(current_dir, name, size))
                        elif line_elems[0] == '$':
                            break
                        else:
                            raise Exception(f"Unknown entry {line_elems[0]}!")
                        line = fd.readline()
                case _:
                    raise Exception(f"Unknown command {command}!")

    return root_dir


def get_dir_sizes(directory: Directory) -> dict:
    dir_sizes = dict()
    for entry in directory.contents:
        if isinstance(entry, Directory):
            dir_sizes.update(get_dir_sizes(entry))
    dir_sizes[directory.name + '-' + str(id(directory))] = directory.size
    return dir_sizes


def solve_one(dir_sizes: dict) -> int:
    sum = 0
    for name, size in dir_sizes.items():
        if size <= 100000:
            sum += size
    return sum


def solve_two(dir_sizes: dict, root_dir, TOTAL_DISK_SPACE, REQUIRED_SPACE) -> tuple:
    candidates = []
    for name, size in dir_sizes.items():
        if TOTAL_DISK_SPACE - (root_dir.size - size) >= REQUIRED_SPACE:
            candidates.append((name, size))
    result = min(candidates, key=lambda dir: dir[1])
    return result


def main():
    TOTAL_DISK_SPACE: int = 70000000
    REQUIRED_SPACE: int = 30000000

    file_path = "data/filesystem.txt"
    root_dir = load_filesystem(file_path)
    print(f"Tree:\n{root_dir}\n\n")
    dir_sizes = get_dir_sizes(root_dir)
    print(f"Directories sizes:\n{pprint.pformat(dir_sizes, indent=4)}\n\n")

    # Part One
    # Find all the directories with a total size of at most 100000.
    # What is the sum of the total sizes of those directories?
    print("PART ONE")
    print(f"Result: {solve_one(dir_sizes)}\n\n")

    # Part Two
    # The total disk space available to the filesystem is 70000000.
    # To run the update, you need unused space of at least 30000000.
    # You need to find a directory you can delete that will free up enough space to run the update.
    #
    # Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update.
    # What is the total size of that directory?
    print("PART TWO")
    unused_space = TOTAL_DISK_SPACE - root_dir.size
    print(f"Root size: {root_dir.size}")
    print(f"Unused space: {unused_space}")
    dir_name, dir_size = solve_two(dir_sizes, root_dir, TOTAL_DISK_SPACE, REQUIRED_SPACE)
    print(f"Result: {(dir_name, dir_size)}")
    print(f"After deletion: {TOTAL_DISK_SPACE - (root_dir.size - dir_size)}")


if __name__ == '__main__':
    main()
