# pylint: disable=unused-import

from time import time
from typing import List, Optional, Any

from kink import inject
from pygame.event import Event

from ...sprites.events import RESET_CARD_TYPE
from ...sprites.cards.card import Card, CardState

from .states import GameStates


class Game:
    def __init__(self):
        self.__revealed = []
        self.__last_time = 0
        self.__time_to_wait = 0.75
        self.__state = GameStates.PLAYER_TURN

    @property
    def state(self) -> GameStates:
        return self.__state

    @state.setter
    def state(self, value: GameStates) -> None:
        self.__state = value

    @property
    def revealed(self) -> List[Card]:
        return self.__revealed

    def reset(self) -> None:
        self.__revealed.clear()
        self.__last_time = 0
        self.__state = GameStates.PLAYER_TURN

    @inject()
    def evaluate(self, events: Optional[Any] = None) -> None:
        if events:
            if len(self.__revealed) >= 2 and self.state is GameStates.PLAYER_TURN:
                card1 = self.__revealed[0]
                card2 = self.__revealed[1]

                if isinstance(card1, Card) and isinstance(card2, Card):
                    if card1.rank == card2.rank and card1.suit == card2.suit:
                        self.__revealed.clear()
                        self.state = GameStates.PLAYER_TURN
                    else:
                        self.__last_time = time()
                        self.state = GameStates.COMPUTER_TURN

        elapsed_time = time() - self.__last_time

        if (
            self.state is GameStates.COMPUTER_TURN
            and elapsed_time >= self.__time_to_wait
        ):
            for index, card in enumerate(self.__revealed):
                if card.state is CardState.REVEALED:
                    params = {"card": card}
                    flip_event = Event(RESET_CARD_TYPE, params)

                    self.__last_time = time()
                    events.post(flip_event)

                    if index == 1:
                        self.__time_to_wait = 0.25

                    break
            else:
                self.state = GameStates.PLAYER_TURN
                self.__revealed.clear()
                self.__time_to_wait = 0.75
