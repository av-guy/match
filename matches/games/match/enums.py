from enum import Enum


class GameState(Enum):
    PLAYER_TURN = 1
    COMPUTER_TURN = 2
    RESET_BOARD = 3
