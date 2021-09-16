import argparse
import urllib.request
from pathlib import Path

content = Path(".env").read_text().strip()


def get_input(day):
    url = f"https://adventofcode.com/2020/day/{day}/input"
    req = urllib.request.Request(url, headers={"Cookie": content})
    return urllib.request.urlopen(req).read().decode()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    args = parser.parse_args()
    Path(f"input{args.day:02}.txt").write_text(get_input(args.day))
