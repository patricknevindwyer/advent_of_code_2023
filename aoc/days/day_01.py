def part_01(filename: str) -> None:
    """
    Read the file, parse out numbers, get the first
    and last, recombine, and we're good.

    :param filename:
    :return:
    """

    with open(filename, "r") as raw:
        data = raw.read().strip()

    running = 0
    for line in data.splitlines():
        digits = [c for c in line if c.isdigit()]
        running += int(f"{digits[0]}{digits[-1]}")
    print(running)


def part_02(filename: str) -> None:
    """
    Rewrite the line with spelled out number
    values, and recalculate.

    :param filename:
    :return:
    """
    with open(filename, "r") as raw:
        data = raw.read().strip()

    running = 0
    for line in data.splitlines():
        line = update_line(line)
        digits = [c for c in line if c.isdigit()]
        selected = f"{digits[0]}{digits[-1]}"
        running += int(selected)
    print(running)


def update_line(line: str) -> str:
    """
    Scan through each line, update all the values
    in all the combinations we can, as the overlaps
    and duplicates may have meaning when scanning
    forwards and backwards.

    :param line:
    :param num_map:
    :return: Updated string
    """
    # Ensure when we scan later we complete
    # any words we may be overwriting (line `twone`)
    num_map = {
        "one": "one1one",
        "two": "two2two",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seven": "seven7seven",
        "eight": "eight8eight",
        "nine": "nine9nine",
    }
    for rep, val in num_map.items():
        line = line.replace(rep, val)
    return line
