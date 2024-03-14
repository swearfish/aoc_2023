from day_02.day02 import is_game_possible, calc_game_power
from utils import read_file_to_list


games = read_file_to_list("day_02/puzzle.txt")


def test_is_possible():
    configuration = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    assert is_game_possible("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", configuration) == 1
    assert is_game_possible("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", configuration) == 2
    assert is_game_possible("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", configuration) == 0
    assert is_game_possible("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", configuration) == 0
    assert is_game_possible("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", configuration) == 5


def test_first_puzzle():
    configuration = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    total_result = 0
    for game in games:
        game_result = is_game_possible(game, configuration)
        total_result += game_result
    assert 0 < total_result
    assert total_result == 2716


def test_calc_power():
    assert calc_game_power("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == 48
    assert calc_game_power("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue") == 12
    assert calc_game_power("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red") == 1560
    assert calc_game_power("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red") == 630
    assert calc_game_power("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green") == 36


def test_second_puzzle():
    total_result = 0
    for game in games:
        power = calc_game_power(game)
        total_result += power
    assert 0 < total_result
    assert total_result == 72227
