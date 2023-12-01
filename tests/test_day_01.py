import pytest
from aoc.days.day_01 import update_line

UPDATES = [
    ("two1nine", "two2two1nine9nine"),
]


@pytest.mark.parametrize("in_str,out_str", UPDATES)
def test_update_line(in_str: str, out_str: str) -> None:
    assert update_line(in_str) == out_str
