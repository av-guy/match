# pylint: disable=all

from os import getcwd
from typing import List, Optional, Callable
from kink import inject, di
from pygame.sprite import Group

from pygame import Surface
from pygame.time import Clock

from .games.match.game import Game
from .components.events import dispatch
from .games.match.dealer import deal_cards


@inject
class GameLoop:
    def __init__(
        self,
        screen: Optional[Surface] = None,
        clock: Optional[Clock] = None,
    ) -> None:

        if not screen or not clock:
            raise ValueError("Screen and clock must be provided")

        self.screen = screen
        self.clock = clock

        self.GREEN = (24, 168, 50)

    def run(self) -> None:
        game_state: Game = di["game_state"]
        groups: List[Group] = di["groups"] or []
        collisions: List[Callable] = di["collisions"] or []

        events = di["events"]
        display = di["display"]
        ui_manager = di["ui_manager"]

        if game_state is None:
            raise ValueError("Game state must be provided")

        while True:
            self.screen.fill(self.GREEN)
            game_state.evaluate()

            for event in events.get():
                dispatch(event.type, event)
                ui_manager.process_events(event)

            for detection in collisions:
                detection()

            delta = self.clock.tick(165) / 1000.0

            ui_manager.update(delta)
            ui_manager.draw_ui(self.screen)

            for group in groups:
                group.update(delta)
                group.draw(self.screen)

            display.update()
