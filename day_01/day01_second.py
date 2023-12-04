
digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def read_digit(instr: str, i: int) -> int | None:
    if '0' <= instr[i] <= '9':
        return int(instr[i])
    for number in digits:
        if instr[i:len(number) + i] == number:
            return digits[number]
    return None


def find_first_digit(instr: str) -> int | None:
    for i in range(0, len(instr)):
        digit = read_digit(instr, i)
        if digit is not None:
            return digit
    return None


def find_last_digit(instr: str) -> int | None:
    for i in range(len(instr), 0, -1):
        digit = read_digit(instr, i-1)
        if digit is not None:
            return digit
    return None


def get_digits(instr: str) -> int:
    first = find_first_digit(instr)
    last = find_last_digit(instr)
    return first * 10 + last


def get_calibration_value(lines: list[str]) -> int:
    result = 0
    for line in lines:
        num = get_digits(line)
        assert num is not None
        result += num
    return result
