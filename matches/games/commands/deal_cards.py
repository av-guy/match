# pylint: disable=no-name-in-module

from pygame.event import Event
from kink import di

from ..events import DEAL_CARDS
from ...components.events import event


@event(DEAL_CARDS)
def deal_cards_event_handler(_: Event) -> None:
    reset_game = di["reset_game"]
    reset_game()
