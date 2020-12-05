import re
from pathlib import Path
from typing import Iterable

import pytest

test = """"""


def seat_id(s: str) -> int:
    row_s = s[:7]
    column_s = s[7:]

    row = row_s.replace("F", "0").replace("B", "1")
    row = int(row, base=2)

    column = column_s.replace("R", "1").replace("L", "0")
    column = int(column, base=2)
    return row * 8 + column


@pytest.mark.parametrize(
    "input, expected",
    (
        ("FBFBBFFRLR", 357),
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
    ),
)
def test_seat_id(input, expected) -> None:

    assert seat_id(input) == expected


if __name__ == "__main__":

    f = Path("input05.txt").read_text().strip()
    all_id = set(seat_id(x) for x in f.splitlines())
    max_id = max(all_id)
    min_id = min(all_id)

    print(max_id)
    print(set(range(min_id, max_id + 1)) - all_id)
