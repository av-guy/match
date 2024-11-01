from enum import Enum


class CardState(Enum):
    HIDDEN = 1
    REVEALED = 2
    FLIPPING_OVER = 3
    FLIPPING_BACK = 4
