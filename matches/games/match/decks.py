from typing import List, Tuple
from itertools import product
from random import sample, shuffle

from ...sprites.cards.enums import CardSuit, CardRank


def create_deck(rows: int, columns: int) -> List[Tuple[CardSuit, CardRank]]:
    if (rows * columns) % 2 != 0:
        raise ValueError("Rows and columns must result in an even number of cards")

    suits = [CardSuit.HEARTS, CardSuit.DIAMONDS, CardSuit.CLUBS, CardSuit.SPADES]

    ranks = [
        CardRank.ACE,
        CardRank.TWO,
        CardRank.THREE,
        CardRank.FOUR,
        CardRank.FIVE,
        CardRank.SIX,
        CardRank.SEVEN,
        CardRank.EIGHT,
        CardRank.NINE,
        CardRank.TEN,
        CardRank.JACK,
        CardRank.QUEEN,
        CardRank.KING,
    ]

    all_cards = list(product(suits, ranks))
    num_cards = (rows * columns) // 2

    sampled_cards = sample(all_cards, num_cards)
    duplicated_cards = sampled_cards * 2

    shuffle(duplicated_cards)
    return duplicated_cards
