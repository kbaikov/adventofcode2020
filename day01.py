import itertools
from pathlib import Path
from typing import Iterable

import pytest

test = """1721
979
366
299
675
1456"""


def mul_if_sum(entries: Iterable[int]) -> int:
    """find the two entries that sum to 2020 and then multiply those two numbers together"""
    for x, y in itertools.combinations(entries, 2):
        if x + y == 2020:
            return x * y
    else:
        raise NotImplementedError


@pytest.mark.parametrize(
    "input, expected",
    (
        (test, 514579),
        (Path("input01.txt").read_text().strip(), 926464),
    ),
)
def test_mul_if_sum(input, expected: int) -> None:
    test_entries = (int(x) for x in input.split())
    assert mul_if_sum(test_entries) == expected


def mul_if_sum_3(entries: Iterable[int]) -> int:
    """the product of the three entries that sum to 2020"""
    for x, y, z in itertools.combinations(entries, 3):
        if x + y + z == 2020:
            return x * y * z
    else:
        raise NotImplementedError


@pytest.mark.parametrize(
    "input, expected",
    (
        (test, 241861950),
        (Path("input01.txt").read_text().strip(), 65656536),
    ),
)
def test_mul_if_sum_3(input, expected: int) -> None:
    test_entries = (int(x) for x in input.split())
    assert mul_if_sum_3(test_entries) == expected


if __name__ == "__main__":

    f = Path("input01.txt").read_text().strip().split()
    print(mul_if_sum((int(x) for x in f)))
    print(mul_if_sum_3((int(x) for x in f)))
