import aoc
import argparse
from art import text2art
from colorama import Fore, Style
import importlib
from itertools import cycle
import os
from random import choice


def options() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Advent of Code daily sections")

    # Which day and part are we running?
    parser.add_argument(
        "-d", "--day", dest="day", default=0, type=int, help="Which day of AOC"
    )
    parser.add_argument(
        "-p",
        "--part",
        dest="part",
        default=1,
        choices=[1, 2],
        type=int,
        help="Which section of a day?",
    )

    # What file are we referencing, if any?
    parser.add_argument(
        "-f", "--file", dest="filename", default=None, help="Data file for AOC Day/part"
    )

    return parser.parse_args()


def colorize(text: str, char: str, st: str) -> str:
    """
    Colorize every instance of a character, replacing
    them in the string. The replacement string(s) will
    be closed out with Fore.RESET and Style.RESET_ALL

    :param text: Input text
    :param char: String to colorize
    :param st: Color and style to apply
    :return: Updated string
    """
    n_char = st + char + Fore.RESET + Style.RESET_ALL
    return text.replace(char, n_char)


def colorize_all(text: str, chars: list[str], st: str) -> str:
    """
    Apply the `colorize` method to every character in the
    `chars` list. This is easier than individually calling
    the `colorize` method on each one.

    :param text:
    :param chars:
    :param st:
    :return:
    """
    t = text
    for char in chars:
        t = colorize(t, char, st)
    return t


def print_header(opts: argparse.Namespace) -> None:
    """
    Print the welcome header.

    :param opts:
    :return:
    """
    # build out the header data
    header = f"""
┌─────────────────────┐
╞══════════╤══════════╡█
│  Day {opts.day:>02}  │  Part {opts.part}  │█
└──────────┴──────────┘█
 ███████████████████████
    """

    # what is our original line width
    width = len(header.splitlines()[1])

    # set up the colorization for larger quantities of characters
    header = colorize(header, "█", Style.DIM + Fore.LIGHTCYAN_EX)
    header = colorize_all(
        header,
        ["┐", "┌", "╞", "└", "╡", "╤", "═", "┴", "─", "│", "┘"],
        Fore.WHITE + Style.BRIGHT,
    )
    header = colorize_all(header, ["Day", "Part"], Style.BRIGHT + Fore.CYAN)

    # now we center all the lines

    center_offset = os.get_terminal_size().columns // 2 - (width // 2)
    spacer = " " * center_offset
    header = "\n".join([spacer + line for line in header.splitlines()])
    print(header)


def banner() -> None:
    """
    Print an AOC Banner.

    :return:
    """
    # Create the letter forms
    font = choice(["ticksslant", "tarty7", "tarty1", "swampland"])

    letters = [
        text2art("A", font=font),
        text2art("O", font=font),
        text2art("C", font=font),
        text2art("2", font=font),
        text2art("0", font=font),
        text2art("2", font=font),
        text2art("3", font=font),
    ]

    # setup colors and apply to lines
    brighten = [choice([Style.BRIGHT, Style.DIM, Style.NORMAL]) for _c in letters]
    colors = cycle(
        [
            Fore.LIGHTRED_EX,
            Fore.LIGHTGREEN_EX,
            Fore.RED,
            Fore.GREEN,
        ]
    )
    styles = list(zip(brighten, colors))

    # join letters
    rows = len(letters[0].splitlines())
    for row in range(rows):
        for letter_idx, letter in enumerate(letters):
            print("".join(styles[letter_idx]), flush=True, end="")
            print(letter.splitlines()[row], end="")
            print(Style.RESET_ALL, Fore.RESET, end="", flush=True)
        print("")


def resolve_function(opts: argparse.Namespace) -> callable:
    """
    Resolve the function we want to call in our solver.

    :param opts:
    :return:
    """
    module_name = f"aoc.days.day_{opts.day:02d}"
    method_name = f"part_{opts.part:02d}"

    # try and load it up
    imp = importlib.import_module(module_name)
    fun = getattr(imp, method_name)

    return fun


def main() -> None:
    banner()
    opts = options()
    print_header(opts)

    # what are we loading?
    fun = resolve_function(opts)

    # let's call it
    fun(opts.filename)
