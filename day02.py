from pathlib import Path
from typing import Iterable, Sequence, Union
import collections
import re

import pytest

test = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


def parse_string(s: str) -> Union[Sequence[str], None]:
    """return the named groups from the string"""
    pattern = (
        r"(?P<minimum>\d+)-(?P<maximum>\d+) (?P<letter>[a-z]+): (?P<password>[a-z]+)"
    )
    m = re.match(pattern, s)
    if m is not None:
        return m.groups()


@pytest.mark.parametrize(
    "input, expected",
    (
        ("1-3 a: abcde", ("1", "3", "a", "abcde")),
        ("1-3 b: cdefg", ("1", "3", "b", "cdefg")),
    ),
)
def test_parse_string(input, expected: int) -> None:
    assert parse_string(input) == expected


def number_of_valid(f: Iterable) -> int:
    """Number of valid passwords matching criteria"""
    valid = 0
    for entry in f:
        minimum, maximum, letter, password = parse_string(entry)
        c = collections.Counter(password)
        if int(minimum) <= c[letter] <= int(maximum):
            valid += 1
    return valid


@pytest.mark.parametrize(
    "input, expected",
    (
        (test.strip().split("\n"), 2),
        (Path("input02.txt").read_text().strip().split("\n"), 416),
    ),
)
def test_number_of_valid(input, expected: int) -> None:
    assert number_of_valid(input) == expected


def possitional_criteria(f):
    valid = 0
    for entry in f:
        index1, index2, letter, password = parse_string(entry)
        index1, index2 = int(index1), int(index2)

        # this could have been a xor.
        # if (password[index1 - 1] == letter) ^ (password[index2 - 1] == letter):
        if password[index1 - 1] == letter and password[index2 - 1] != letter:
            valid += 1
        elif password[index2 - 1] == letter and password[index1 - 1] != letter:
            valid += 1
    return valid


@pytest.mark.parametrize(
    "input, expected",
    (
        (test.strip().split("\n"), 1),
        (Path("input02.txt").read_text().strip().split("\n"), 688),
    ),
)
def test_possitional_criteria(input, expected: int) -> None:
    assert possitional_criteria(input) == expected


if __name__ == "__main__":

    f = Path("input02.txt").read_text().strip().split("\n")
    print(number_of_valid(f))
    print(possitional_criteria(f))
