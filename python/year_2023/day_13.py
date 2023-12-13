from typing import Iterable, Optional
from operator import eq, ne


def part_1(input: str) -> int:
    return sum(map(reflection_1, input.rstrip().split("\n\n")))  # type: ignore


def reflection_1(input: str) -> Optional[int]:
    rows = input.splitlines()
    m = len(rows)
    for i in range(1, m):
        if all(map(eq, rows[i - 1 :: -1], rows[i:])):
            return i * 100

    cols = list(zip(*rows))
    n = len(cols)
    for j in range(1, n):
        if all(map(eq, cols[j - 1 :: -1], cols[j:])):
            return j


def part_2(input: str) -> int:
    return sum(map(reflection_2, input.rstrip().split("\n\n")))  # type: ignore


def reflection_2(input: str) -> Optional[int]:
    rows = input.splitlines()
    for i in range(1, len(rows)):
        if sum_diffs_2d(rows[i - 1 :: -1], rows[i:]) == 1:
            return i * 100

    cols = tuple(zip(*rows))
    for j in range(1, len(cols)):
        if sum_diffs_2d(cols[j - 1 :: -1], cols[j:]) == 1:
            return j


def sum_diffs_2d(a: Iterable[Iterable[str]], b: Iterable[Iterable[str]]) -> int:
    return sum(map(sum_diffs_1d, a, b))


def sum_diffs_1d(a: Iterable[str], b: Iterable[str]) -> int:
    return sum(map(ne, a, b))


def test_part_1_example_1():
    assert part_1(EXAMPLE_1) == 405


def test_part_1_input():
    with open("../testdata/year_2023/day_13.txt", "r") as f:
        assert part_1(f.read()) == 41859


def test_part_2_example_1():
    assert part_2(EXAMPLE_1) == 400


def test_part_2_input():
    with open("../testdata/year_2023/day_13.txt", "r") as f:
        assert part_2(f.read()) == 30842


EXAMPLE_1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
