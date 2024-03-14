def get_worth(winning: set[int], own: set[int]) -> int:
    common = winning.intersection(own)
    return len(common)


def read_card(instr: str) -> tuple[set[int], set[int]]:
    numbers = instr.split(":")[1].strip().split("|")
    set1 = set(map(int, numbers[0].split()))
    set2 = set(map(int, numbers[1].split()))
    return set1, set2


def get_card_worth(instr: str) -> int:
    winning, own = read_card(instr)
    worth = get_worth(winning, own)
    return worth


def get_card_points(instr: str) -> int:
    worth = get_card_worth(instr)
    points = 2 ** (worth-1) if 0 < worth else 0
    return points


def play(in_cards: list[str]) -> list[int]:
    card_worth = [get_card_worth(line) for line in in_cards]
    num_cards = len(card_worth)
    cards = [1 for i in range(0, num_cards)]
    for i in range(0, num_cards):
        worth = card_worth[i]
        if 0 < worth and i < num_cards-1:
            for j in range(i+1, min(num_cards, i+worth+1)):
                cards[j] += cards[i]
    return cards