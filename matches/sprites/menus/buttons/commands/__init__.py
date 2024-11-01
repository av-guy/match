from .reset_game import reset_game_event

from .....components.events import initialize


def initialize_handlers() -> None:
    initialize(reset_game_event)
