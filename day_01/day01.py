def find_numbers(instr: str) -> str:
    result = ""
    for ch in instr:
        if '0' <= ch <= '9':
            result += ch
    return result


def get_relevant_number(instr: str) -> int | None:
    numbers = find_numbers(instr)
    if 0 == len(numbers):
        return None
    else:
        return int(numbers[0] + numbers[-1])


def get_calibration_value(lines: list[str]) -> int:
    result = 0
    for line in lines:
        num = get_relevant_number(line)
        assert num is not None
        result += num
    return result
