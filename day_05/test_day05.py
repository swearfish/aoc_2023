from day_05.day05 import get_locations_range, get_locations_single
from utils import read_file_to_list

example = read_file_to_list("day_05/example.txt")
puzzle = read_file_to_list("day_05/puzzle.txt")


def test_example_1():
    locations = get_locations_single(example)
    assert len(locations) == 4
    assert locations[0] == 82
    assert locations[1] == 43
    assert locations[2] == 86
    assert locations[3] == 35
    assert min(locations) == 35


def test_puzzle_1():
    locations = get_locations_single(puzzle)
    assert min(locations) == 323142486


def test_example_2():
    min_location = get_locations_range(example)
    assert min_location == 46


def test_puzzle_2():
    min_location = get_locations_range(puzzle)
    assert min_location == 323142486
