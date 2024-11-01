from pygame.event import Event

from ....events import RESET_GAME

from .....components.events import event
from .....games.match.dealer import reset_cards


@event(RESET_GAME)
def reset_game_event(_: Event) -> None:
    reset_cards()
