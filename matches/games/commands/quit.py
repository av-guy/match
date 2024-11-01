# pylint: disable=no-name-in-module

import sys

from pygame.event import Event
from pygame.locals import QUIT

from ...components.events import event


@event(QUIT)
def quit_game(_: Event) -> None:
    sys.exit()
