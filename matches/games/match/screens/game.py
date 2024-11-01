# pylint: disable=wrong-import-position
# pylint: disable=unused-import
# pylint: disable=import-outside-toplevel
# pylint: disable=no-name-in-module

from pygame.rect import Rect
from kink import di

from ....sprites.menus.buttons.button import GameButton
from ....sprites.menus.buttons.enums import ButtonType

from ..rules import reveal_rules, left_mouse_button_rules
from ..game import Game
from ..decks import create_deck
from ..dealer import deal_cards
from ...events import DEAL_CARDS


def reset() -> None:
    cards_sprites_group = di["cards_sprite_group"]
    cards_sprites_group.empty()

    rows = di["card_rows"]
    columns = di["card_columns"]

    deck = create_deck(rows, columns)

    di["game_deck"] = deck
    deal_cards(deck, rows)


def initialize(rows: int, columns: int) -> None:
    di["game_state"] = Game()

    di["card_rows"] = rows
    di["card_columns"] = columns

    di["reset_game"] = reset

    di["lmb_rules"] = left_mouse_button_rules
    di["drag_rules"] = lambda: False
    di["reveal_rules"] = reveal_rules

    GameButton(
        relative_rect=Rect((10, 10), (100, 50)),
        text="Reset Game",
        button_type=ButtonType.RESET_GAME,
    )

    from ....games.match.controls import initialize_handlers as init_controls
    from ....sprites.cards.commands import initialize_handlers as init_card_handlers

    from ....sprites.pointers.commands import (
        initialize_handlers as init_pointer_handlers,
    )

    from ....sprites.menus.buttons.commands import (
        initialize_handlers as init_button_handlers,
    )

    init_controls()
    init_card_handlers()
    init_pointer_handlers()
    init_button_handlers()

    events = di["events"]
    events.post(DEAL_CARDS)
