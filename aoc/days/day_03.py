from typing import Union


def part_01(filename: str) -> None:
    num_locs, sym_locs = parse_schematic(filename)

    running = 0
    for loc, num in num_locs.items():
        if is_number_adjacent_to_symbol(sym_locs, loc, num):
            running += num

    print(f"{running} part sum total")


def part_02(filename: str) -> None:
    num_locs, sym_locs = parse_schematic(filename)

    # let's track all the adjacent numbers and gears
    gear_candidates = {}

    for loc, num in num_locs.items():
        candidate = get_gear_adjacent(sym_locs, loc, num)
        if candidate is not None:
            if candidate not in gear_candidates:
                gear_candidates[candidate] = []
            gear_candidates[candidate].append(num)

    # now check all candidate gears
    running = 0
    for c_loc, gear_nums in gear_candidates.items():
        if len(gear_nums) == 2:
            gear_ratio = gear_nums[0] * gear_nums[1]
            running += gear_ratio

    print(f"{running} gear ratio totals")


def get_gear_adjacent(
    symbol_dict: dict[tuple[int, int], str], num_loc: tuple[int, int], num: int
) -> Union[None, tuple[int, int]]:
    """
    This is akin to the `is_number_adjacent_to_symbol`, but now we want to
    find any gear adjacent to our number.

    :param symbol_dict:
    :param num_loc:
    :param num:
    :return:
    """
    neighbors = number_neighbors(num_loc, num)

    for neighbor in neighbors:
        if neighbor in symbol_dict and symbol_dict[neighbor] == "*":
            return neighbor
    return None


def is_number_adjacent_to_symbol(
    symbol_dict: dict[tuple[int, int], str], num_loc: tuple[int, int], num: int
) -> bool:
    """
    Is a number adjacent to a symbol?

    :param symbol_dict:
    :param num_loc:
    :param num:
    :return:
    """
    neighbors = number_neighbors(num_loc, num)

    for neighbor in neighbors:
        if neighbor in symbol_dict:
            return True
    return False


def number_neighbors(loc: tuple[int, int], num: int) -> list[tuple[int, int]]:
    """
    Generate the list of neighbor points for a number
    at a location.

    >>> number_neighbors((0, 0), 12)
    [(-1, -1), (0, -1), (1, -1), (2, -1), (-1, 0), (2, 0), (-1, 1), (0, 1), (1, 1), (2, 1)]

    :param loc:
    :param num:
    :return:
    """
    # basic coordinates
    n_len = len(f"{num}")
    x = loc[0]
    y = loc[1]

    # boundaries
    left = x - 1
    right = x + n_len
    top = y - 1
    bottom = y + 1

    neighbors = []

    # top
    for x_idx in range(left, right + 1):
        neighbors.append((x_idx, top))

    # left
    neighbors.append((left, y))

    # right
    neighbors.append((right, y))

    # bottom
    for x_idx in range(left, right + 1):
        neighbors.append((x_idx, bottom))

    return neighbors


def parse_schematic(
    filename: str,
) -> tuple[dict[tuple[int, int], int], dict[tuple[int, int], str]]:
    """
    Parse the engine schematic, returning two grid dictionaries:

     - Location of numbers (by the first character) as key, number as value
     - Location of Symbols as key, symbol as value

    :param filename:
    :return:
    """

    symbol_dict = {}
    number_accumulator = []
    number_loc = None
    number_dict = {}

    with open(filename, "r") as raw:
        data = raw.read()

    for row_idx, line in enumerate(data.split("\n")):
        # clear the accumulators
        if len(number_accumulator) > 0:
            number_dict[number_loc] = int("".join(number_accumulator))
        number_accumulator = []
        number_loc = None

        for col_idx, char in enumerate(line):
            if char.isdigit():
                number_accumulator.append(char)
                if number_loc is None:
                    number_loc = (col_idx, row_idx)
            else:
                # clear the accumulator
                if len(number_accumulator) > 0:
                    number_dict[number_loc] = int("".join(number_accumulator))
                number_accumulator = []
                number_loc = None

                # track symbols
                if char != ".":
                    symbol_dict[(col_idx, row_idx)] = char

    # one last clear of the accumulator
    if len(number_accumulator) > 0:
        number_dict[number_loc] = int("".join(number_accumulator))

    return number_dict, symbol_dict
