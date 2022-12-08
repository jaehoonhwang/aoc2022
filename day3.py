from aoc import files

input_file_name = "day3.txt"

UPPER_BASE = ord("A") - 27
LOWER_BASE = ord("a") - 1
GROUP = 3


def get_value(ch: str) -> int:
    if not ch.isalpha():
        raise RuntimeError("Something went wrong {}".format(ch))
    return ord(ch) - UPPER_BASE if ch.isupper() else ord(ch) - LOWER_BASE


def get_duplicate(line: str) -> str:
    mid_point = len(line) // 2
    lhs, rhs = line[:mid_point], line[mid_point:]

    for ch in lhs:
        if ch in rhs:
            return ch

    return ""


def get_duplicates(lines: list[str]) -> str:
    lead: str = lines[0]
    checkers: list[str] = lines[1:]
    found: bool = True
    for ch in lead:
        for check in checkers:
            if ch not in check:
                found = False
                break

        if found:
            return ch

        found = True

    return ""


def solution_one(lines: list[str]) -> int:
    ret = 0

    for line in lines:
        dupe = get_duplicate(line)
        ret += get_value(dupe)

    return ret


def solution_two(lines: list[str]) -> int:
    ret = 0

    for i in range(len(lines)//GROUP):
        dupe = get_duplicates(lines[i*GROUP:(i+1)*GROUP])
        ret += get_value(dupe)

    return ret


def day3():
    lines = files.read_lines(input_file_name)

    print("Solution for part 1: {}".format(solution_one(lines)))
    print("Solution for part 2: {}".format(solution_two(lines)))


if __name__ == "__main__":
    day3()
