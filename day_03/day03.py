import re
from functools import reduce
from operator import mul


def collect_numbers(string: str) -> list[tuple[int, int, int]]:
    pattern = r"\d+"
    matches = re.finditer(pattern, string)
    result = [(match.start(), match.end(), int(match.group())) for match in matches]
    return result


def has_symbol(line: int, start: int, end: int, schematic: list[str]) -> bool:
    if line < 0:
        return False
    if len(schematic) <= line:
        return False
    row = schematic[line]
    start = max(0, start)
    end = min(len(row), end)
    for ch in row[start:end]:
        if ch != '.' and (ch < '0' or ch > '9'):
            return True
    return False


def find_part_number(schematic: list[str]) -> int:
    result = 0
    for line in range(0, len(schematic)):
        row = schematic[line]
        numbers = collect_numbers(row)
        for start, end, number in numbers:
            has_symbol_top = has_symbol(line - 1, start - 1, end + 1, schematic)
            has_symbol_center = has_symbol(line, start - 1, end + 1, schematic)
            has_symbol_bottom = has_symbol(line + 1, start - 1, end + 1, schematic)
            if has_symbol_bottom or has_symbol_center or has_symbol_top:
                result += number
    return result


def is_adjacent(number: tuple[int, int, int, int], gear: tuple[int, int]) -> bool:
    if 1 < abs(gear[0] - number[0]):
        return False
    return number[1] - 1 <= gear[1] < number[2] + 1


def find_gear_ratio(schematic: list[str]) -> int:
    result = 0
    numbers = []
    gears = []
    for line in range(0, len(schematic)):
        row = schematic[line]
        for start, end, number in collect_numbers(row):
            numbers.append((line, start, end, number))
        for i in range(0, len(row)):
            if row[i] == '*':
                gears.append((line, i))
    for gear in gears:
        adjacent_numbers = []
        for number in numbers:
            if is_adjacent(number, gear):
                adjacent_numbers.append(number[3])
        if 1 < len(adjacent_numbers):
            gear_ratio = reduce(mul, adjacent_numbers)
            result += gear_ratio
    return result
