import re
from pathlib import Path
from typing import Iterable

import pytest

test = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def check_answers(f: str) -> int:
    y = 0
    for group in f.split("\n\n"):
        group_answers = set()
        for person in group.splitlines():
            for answer in person:
                group_answers.add(answer)
        y += len(group_answers)
    return y


@pytest.mark.parametrize(
    "input, expected",
    (
        (test, 11),
        (Path("input06.txt").read_text().strip(), 6585),
    ),
)
def test_check_answers(input, expected) -> None:

    assert check_answers(input) == expected


def check_answers2(f: str) -> int:
    y = 0
    for group in f.split("\n\n"):
        possible_answers = set("abcdefghijklmnopqrstuvwxyz")
        for person in group.splitlines():
            possible_answers &= set(person)
        y += len(possible_answers)
    return y


@pytest.mark.parametrize(
    "input, expected",
    (
        (test, 6),
        (Path("input06.txt").read_text().strip(), 3276),
    ),
)
def test_check_answers2(input, expected) -> None:

    assert check_answers2(input) == expected


if __name__ == "__main__":

    f = Path("input06.txt").read_text().strip()
    print(check_answers(f))
    print(check_answers2(f))
