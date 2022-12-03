from aoc import files

input_file_name = "day1.txt"


def convert_calories(calories: list[str]) -> list[int]:
    ret = []
    current = 0
    for calory in calories:
        if calory == "":
            ret.append(current)
            current = 0
            continue

        current += int(calory)

    return ret


def solution_one(calories: list[str]) -> int:
    elfs = convert_calories(calories)

    return max(elfs)


def solution_two(calories: list[str], top: int) -> int:
    elfs = convert_calories(calories)

    return sum(elfs[-top:])


def day1():
    lines = files.read_lines(input_file_name)
    top = 3

    print("Solution for part 1: {}".format(solution_one(lines)))
    print("Solution for part 2: {}".format(solution_two(lines, top)))


if __name__ == "__main__":
    day1()
