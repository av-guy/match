# pylint: disable=no-name-in-module

from typing import Any, List
from pygame.event import Event
from pygame.sprite import Group

from pygame.locals import MOUSEBUTTONDOWN
from kink import inject, di

from ....sprites.events import FLIP_CARD
from ....sprites.cards.card import Card

from ....components.events import event
from ....components.focus import focus
from ....components.collisions import collision

from ... import rules

from ..focuses.enums import FocusAreas

POINTERS: Group = di["pointers_sprite_group"]
CARDS: Group = di["cards_sprite_group"]
BUTTONS: Group = di["buttons_sprite_group"]


@event(MOUSEBUTTONDOWN)
@collision(POINTERS, CARDS)
@focus(FocusAreas.GAME_BOARD)
@rules("lmb_rules")
@inject()
def left_btn_press_card(
    card_collisions: List[Card],
    btn_press_event: Event,
    events: Any,
) -> None:
    if btn_press_event.button == 1:
        for focused_card in card_collisions:
            params = {"card": focused_card, "player_origin": True}
            flip_event = Event(FLIP_CARD.type, params)
            events.post(flip_event)
