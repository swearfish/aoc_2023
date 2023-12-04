from .day01_second import get_digits, get_calibration_value, find_first_digit
from utils import read_file_to_list


def test_find_first_digit():
    assert find_first_digit("one2") == 1
    assert find_first_digit("1") == 1
    assert find_first_digit("1234567890") == 1
    assert find_first_digit("1zero") == 1
    assert find_first_digit("a1zero") == 1
    assert find_first_digit("aonezero") == 1


def test_get_digits():
    assert get_digits("one2") == 12
    assert get_digits("1") == 11
    assert get_digits("1234567890") == 10
    assert get_digits("1zero") == 10
    assert get_digits("twothree") == 23
    assert get_digits("twoathreeb") == 23
    assert get_digits("aaaatwoaaaathreebbb") == 23
    assert get_digits("twothre") == 22
    assert get_digits("fourfive") == 45
    assert get_digits("sixseven") == 67
    assert get_digits("eightnine") == 89


def test_sample():
    inputs = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2",
              "zoneight234", "7pqrstsixteen"]
    outputs = [29, 83, 13, 24, 42, 14, 76]
    expected_result = sum(outputs)
    actual_result = 0
    for i in range(0, len(inputs)):
        instr = inputs[i]
        digits = get_digits(instr)
        assert digits == outputs[i]
        actual_result += digits
    assert actual_result == expected_result
    assert get_calibration_value(inputs) == expected_result


def test_puzzle_input():
    input_file = read_file_to_list("day_02/puzzle.txt")
    calibration_value = get_calibration_value(input_file)
    assert calibration_value == 53592