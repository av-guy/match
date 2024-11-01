from kink import di
from .enums import FocusAreas


def focus_game_board() -> None:
    di["focus_area"] = FocusAreas.GAME_BOARD


def focus_pause_menu() -> None:
    di["focus_area"] = FocusAreas.PAUSE_MENU
