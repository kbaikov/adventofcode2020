from pathlib import Path
from typing import Optional
import itertools

import pytest

test = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def wrong_number(f: str, current) -> int:
    lookbehind = 0
    nums = [int(x) for x in f.split()]
    while True:
        if not any(
            x + y == nums[current]
            for x, y in list(itertools.combinations(nums[lookbehind:current], 2))
        ):
            return nums[current]
        current += 1
        lookbehind += 1


@pytest.mark.parametrize(
    "input, expected",
    (
        ((test, 5), 127),
        ((Path("input09.txt").read_text().strip(), 25), 177777905),
    ),
)
def test_wrong_number(input, expected) -> None:

    assert wrong_number(*input) == expected


def long_sum(f: str, number) -> Optional[int]:
    start = 0
    end = 0
    nums = [int(x) for x in f.split()]
    for start in range(len(f)):
        for end in range(start + 1, len(f)):
            new_list = nums[start : end + 1]
            s = sum(new_list)
            if s == number:
                return min(new_list) + max(new_list)
            elif s > number:
                break
    return None


@pytest.mark.parametrize(
    "input, expected",
    (
        ((test, 127), 62),
        ((Path("input09.txt").read_text().strip(), 177777905), 23463012),
    ),
)
def test_long_sum(input, expected) -> None:

    assert long_sum(*input) == expected


if __name__ == "__main__":

    f = Path("input09.txt").read_text().strip()
    print(wrong_number(f, 25))
    print(long_sum(f, 177777905))
