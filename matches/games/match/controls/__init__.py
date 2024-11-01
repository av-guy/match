from .mouse import left_btn_press_card
from ....components.events import initialize


def initialize_handlers() -> None:
    initialize(left_btn_press_card)
