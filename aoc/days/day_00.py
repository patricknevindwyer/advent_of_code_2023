from art import tprint
from random import choice


def part_01(filename: str = None) -> None:
    """
    Day 00 Part 01.

    :param filename: Source file with problem data
    :return:
    """
    tprint(
        "Advent", font=choice(["isometric1", "isometric2", "isometric3", "isometric4"])
    )
    tprint("of", font=choice(["isometric1", "isometric2", "isometric3", "isometric4"]))
    tprint(
        "Code", font=choice(["isometric1", "isometric2", "isometric3", "isometric4"])
    )
    tprint(
        "2020", font=choice(["isometric1", "isometric2", "isometric3", "isometric4"])
    )


def part_02(filename: str = None) -> None:
    """
    Day 00 Part 02.

    :param filename: Source file with problem data
    :return:
    """
    print("Hi there!")
