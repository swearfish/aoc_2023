from day_03.day03 import find_part_number, find_gear_ratio
from utils import read_file_to_list


def test_find_part_number():
    schematic = read_file_to_list("day_03/example.txt")
    part_number = find_part_number(schematic)
    assert part_number == 4361


def test_first_puzzle():
    schematic = read_file_to_list("day_03/puzzle.txt")
    part_number = find_part_number(schematic)
    assert part_number == 539590


def test_gear_ratio():
    schematic = read_file_to_list("day_03/example.txt")
    part_number = find_gear_ratio(schematic)
    assert part_number == 467835


def test_second_puzzle():
    schematic = read_file_to_list("day_03/puzzle.txt")
    part_number = find_gear_ratio(schematic)
    assert part_number == 80703636
