from typing import Any, Optional
from kink import di, inject

from pygame.sprite import Group
from pygame.event import Event

from .game import Game
from .states import GameStates

from ...sprites.cards.card import Card
from ...sprites.cards.models import CardData
from ...sprites.events import RESET_CARD_TYPE


@inject()
def deal_cards(deck, rows, game_state: Optional[Game] = None) -> None:
    x_offset = 0 + di["screen_width"] // 4
    y_offset = 0 + di["screen_height"] // 6

    for index, card in enumerate(deck):
        if index != 0 and index % rows == 0:
            x_offset = 0 + di["screen_width"] // 4
            y_offset += 125

        Card(CardData(card[0], card[1], x_offset, y_offset))
        x_offset += 100

    if game_state is not None:
        game_state.reset()


@inject()
def reset_cards(
    cards_sprite_group: Optional[Group] = None,
    events: Any = None,
    game_state: Optional[Game] = None,
) -> None:
    if game_state:
        game_state.state = GameStates.RESETTING_CARDS

    if events and cards_sprite_group:
        cards = cards_sprite_group.sprites()

        for index, card in enumerate(cards):
            params = {"card": card, "last": index == len(cards) - 1}
            events.post(Event(RESET_CARD_TYPE, params))
