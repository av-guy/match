from dataclasses import dataclass
from ..enums import CardRank, CardSuit


@dataclass
class CardData:
    suit: CardSuit
    rank: CardRank
    x: int
    y: int
