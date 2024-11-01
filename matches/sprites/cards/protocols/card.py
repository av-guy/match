# pylint: disable=no-name-in-module

from typing import Protocol, Any, Tuple
from pygame.rect import Rect
from ..enums import CardRank, CardSuit, CardState


class CardProtocol(Protocol):
    state: CardState
    rank: CardRank
    suit: CardSuit
    image: Any
    angle: float
    width: int
    rect: Rect
    position: Tuple[int, int]
    revealed: bool
