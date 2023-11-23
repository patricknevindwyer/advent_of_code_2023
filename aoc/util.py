def count_hole_in_string(text: str, hole: str = " ") -> int:
    """
    Count the number of holes in a given string.

    >>> count_hole_in_string("a b c")
    2

    >>> count_hole_in_string(".A..B.C ", hole=".")
    4

    :param text: Text of a grid, string, etc
    :param hole: Character reprenting a hole
    :return: Number of holes
    """
    return text.count(hole)
