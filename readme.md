
Setup a local install:

```bash
pip install -e . 
```

And run code for a day:

```bash
aoc --day 1 --part 1
```

# Days

|      | Day | Part 01         | Part 02         |
|------|-----|-----------------|-----------------|
| 🌟🌟 | 01  | `aoc -d 1 -p 1` | `aoc -d 1 -p 2` |
| 🌟🌟 | 02  | `aoc -d 2 -p 1` | `aoc -d 2 -p 2` |
| 🌟🌟 | 03  | `aoc -d 3 -p 1` | `aoc -d 3 -p 2` |


# Structure

The `aoc` entry point script (which maps to the [entry.py](aoc/entry.py) file) will
automatically load modules and functions from the `aoc.days` sub-modules. Each day
is a stand-alone file with a `part_01` and `part_02` method.

Each part of each days follows a similar structure:

```python
def part_01(filename: str = None) -> None:
    """
    Day 00 Part 01.

    :param filename: Source file with problem data
    :return:
    """
    ...
```

Where the incoming parameter is the filename of the problem data for the
Day and Part. The file data can be specified with the `-f` command line
parameter.

## Tests

Individual test files are in the `tests` directory, and _doctests_ are integrated
into as well. Run all tests with `pytest`.



