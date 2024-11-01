from .motion import move_mouse
from ....components.events import initialize


def initialize_handlers() -> None:
    initialize(move_mouse)
