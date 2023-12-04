from .day01_first import find_numbers, get_relevant_number, get_calibration_value
from utils import read_file_to_list


def test_find_numbers():
    assert find_numbers("") == ""
    assert find_numbers("12") == "12"
    assert find_numbers("1") == "1"
    assert find_numbers("1234567890") == "1234567890"
    assert find_numbers("1a2") == "12"
    assert find_numbers("a12") == "12"
    assert find_numbers("12q") == "12"


def test_sample_input_find():
    assert find_numbers("1abc2") == "12"
    assert find_numbers("pqr3stu8vwx") == "38"
    assert find_numbers("a1b2c3d4e5f") == "12345"
    assert find_numbers("treb7uchet") == "7"


def test_sample_input_relevant_numbers():
    assert get_relevant_number("1abc2") == 12
    assert get_relevant_number("pqr3stu8vwx") == 38
    assert get_relevant_number("a1b2c3d4e5f") == 15
    assert get_relevant_number("treb7uchet") == 77


def test_sample_input_calibration():
    assert get_calibration_value(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]) == 12 + 38 + 15 + 77


def test_puzzle_input():
    input_file = read_file_to_list("day_01/puzzle.txt")
    calibration_value = get_calibration_value(input_file)
    assert calibration_value == 55621