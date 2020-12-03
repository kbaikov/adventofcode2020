from pathlib import Path
from typing import Iterable

import pytest

test = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def parse_to_list_of_lists(f: str) -> list:
    """parse into list of lists"""

    return [[x for x in lst] for lst in f.split()]


@pytest.mark.parametrize(
    "input, expected",
    (
        (test.strip(), 11),
        (Path("input03.txt").read_text().strip(), 323),
    ),
)
def test_parse_to_list_of_lists(input, expected: int) -> None:
    assert len(parse_to_list_of_lists(input)) == expected


def traverse(tree_map: list, right: int, down: int) -> int:
    """traversing the map using given slope"""
    x = 0
    y = 0
    max_y = len(tree_map)
    mod_x = len(tree_map[0])
    tree = 0
    while y < max_y:
        if tree_map[y][x] == "#":
            tree += 1
        x = (x + right) % mod_x
        y += down
    return tree


@pytest.mark.parametrize(
    "input, expected",
    (
        (test.strip(), 7),
        (Path("input03.txt").read_text().strip(), 191),
    ),
)
def test_traverse(input, expected: int) -> None:
    lst = parse_to_list_of_lists(input)
    assert traverse(lst, 3, 1) == expected


if __name__ == "__main__":

    f = Path("input03.txt").read_text().strip()
    lst = parse_to_list_of_lists(f)
    print(traverse(lst, 3, 1))

    prod = 1
    for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        prod *= traverse(lst, right, down)

    print(prod)  # 1478615040
