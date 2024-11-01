from .flip import flip_card
from .reset import reset_card

from ....components.events import initialize


def initialize_handlers() -> None:
    initialize(flip_card)
    initialize(reset_card)
