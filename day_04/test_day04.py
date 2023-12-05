from day_04.day04 import get_card_worth, get_card_points, play
from utils import read_file_to_list

example = read_file_to_list("day_04/example.txt")
puzzle = read_file_to_list("day_04/puzzle.txt")


def test_example_1():
    expected_points = [8, 2, 2, 1, 0, 0]
    expected_pile_worth = sum(expected_points)
    assert expected_pile_worth == 13
    pile_worth = 0
    for line, points in zip(example, expected_points):
        card_points = get_card_points(line)
        assert card_points == points
        pile_worth += card_points
    assert pile_worth == expected_pile_worth


def test_puzzle_1():
    card_points = [get_card_points(line) for line in puzzle]
    pile_worth = sum(card_points)
    assert 0 < pile_worth
    assert pile_worth == 25004


def test_example_2():
    cards = play(example)
    assert cards[0] == 1
    assert cards[1] == 2
    assert cards[2] == 4
    assert cards[3] == 8
    assert cards[4] == 14
    assert cards[5] == 1
    assert sum(cards) == 30


def test_puzzle_2():
    cards = play(puzzle)
    total = sum(cards)
    assert total == 14427616
