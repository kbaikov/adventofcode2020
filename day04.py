import re
from pathlib import Path

import pytest

test = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


def parse_passport(passport_string: str) -> dict:
    """Parse a string to dict"""
    return {
        entry.strip().split(":")[0]: entry.strip().split(":")[1]
        for entry in passport_string.split()
    }


@pytest.mark.parametrize(
    "input",
    (
        (test.strip().split("\n\n")[0]),
        # (Path("input03.txt").read_text().strip(), 191),
    ),
)
def test_parse_passport(input) -> None:
    expected = {
        "ecl": "gry",
        "pid": "860033327",
        "eyr": "2020",
        "hcl": "#fffffd",
        "byr": "1937",
        "iyr": "2017",
        "cid": "147",
        "hgt": "183cm",
    }
    assert parse_passport(input) == expected


def is_valid(p: dict) -> bool:
    patterns = {
        "hgt": re.compile(r"^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$"),
        "hcl": re.compile(r"^#([a-f0-9]){6}$"),
        "pid": re.compile(r"^\d{9}$"),
        "byr": re.compile(r"(19[2-8][0-9]|199[0-9]|200[0-2])"),
        "iyr": re.compile(r"(201[0-9]|2020)"),
        "eyr": re.compile(r"(202[0-9]|2030)"),
        "ecl": re.compile(r"^amb|blu|brn|gry|grn|hzl|oth$"),
    }

    for field in ("ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"):
        if field not in p.keys():
            return False
        elif not patterns[field].match(p[field]):
            return False

    return True


def test_is_valid() -> None:
    expected = {
        "ecl": "gry",
        "pid": "860033327",
        "eyr": "2020",
        "hcl": "#fffffd",
        "byr": "1937",
        "iyr": "2017",
        "cid": "147",
        "hgt": "183cm",
    }
    assert is_valid(expected) is True


def check_batch(f: str) -> int:
    valid = 0
    for passport in f.split("\n\n"):
        if is_valid(parse_passport(passport)):
            valid += 1
    return valid


test_invalid = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

test_valid = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""


@pytest.mark.parametrize(
    "input, expected",
    (
        (test, 2),
        (test_invalid, 0),
        (test_valid, 4),
        (Path("input04.txt").read_text().strip(), 198),
    ),
)
def test_check_batch(input, expected) -> None:

    assert check_batch(input) == expected


if __name__ == "__main__":

    f = Path("input04.txt").read_text().strip()
    print(check_batch(f))
