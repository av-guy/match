from pygame.event import Event
from kink import di

from ...sprites.cards.card import Card, CardState

from .states import GameStates
from .game import Game


def reveal_rules(flip_event: Event) -> bool:
    game_state: Game = di["game_state"]

    revealed = game_state.revealed
    player_origin = flip_event.player_origin

    card: Card = flip_event.card

    if not player_origin:
        return True

    if (
        game_state.state is GameStates.COMPUTER_TURN
        or game_state.state is GameStates.RESETTING_CARDS
    ):
        return False

    if (
        len(revealed) < 2
        and card not in revealed
        and card.state is not CardState.REVEALED
    ):
        revealed.append(card)
        return True

    return False


def left_mouse_button_rules(*_, **__) -> bool:
    game_state: Game = di["game_state"]
    return game_state.state is GameStates.PLAYER_TURN
