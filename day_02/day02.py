from functools import reduce
from operator import mul


def is_possible(game: list[dict[str, int]], bag: dict[str, int]) -> bool:
    for round in game:
        for cube in round:
            if cube not in bag:
                return False
            if bag[cube] < round[cube]:
                return False
    return True


def find_minimal_set(game: list[dict[str, int]]) -> dict[str, int]:
    result = {}
    for round in game:
        for cube in round:
            if cube not in result:
                result[cube] = round[cube]
            else:
                result[cube] = max(result[cube], round[cube])
    return result


def decode_game_rounds(input_string: str) -> list[dict[str, int]]:
    groups = input_string.split(";")
    result = []

    for group in groups:
        colors = group.split(",")
        color_dict = {}

        for color in colors:
            quantity, color_name = color.strip().split(" ")
            color_dict[color_name] = int(quantity)

        result.append(color_dict)

    return result


def is_game_possible(input_string: str, configuration: dict[str, int]) -> int:
    game_id_text, rounds_text = input_string.strip().split(":")
    game_text, game_id = game_id_text.strip().split(" ")
    rounds = decode_game_rounds(rounds_text)
    if is_possible(rounds, configuration):
        return int(game_id)
    return 0


def find_minimal_set_for_game(input_string: str) -> dict[str, int]:
    game_id_text, rounds_text = input_string.strip().split(":")
    rounds = decode_game_rounds(rounds_text)
    return find_minimal_set(rounds)


def calc_game_power(input_string: str) -> int:
    minimal_set = find_minimal_set_for_game(input_string)
    values = list(minimal_set.values())
    power = reduce(mul, values)
    return power
