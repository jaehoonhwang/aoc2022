def read_lines(file_name: str) -> list[str]:
    """Read input lines from files; simple for AOC event. """
    lines: list[str] = []
    file_name = "testdata/" + file_name
    with open(file_name, 'r') as f:
        lines = f.readlines()

    return [line.rstrip() for line in lines]
