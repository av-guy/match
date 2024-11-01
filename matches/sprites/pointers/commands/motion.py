# pylint: disable=no-name-in-module

from typing import Optional, Any
from kink import inject

from pygame.sprite import Group
from pygame.event import Event
from pygame.locals import MOUSEMOTION

from ....components.events import event
from ..pointer import Pointer


@event(MOUSEMOTION)
@inject()
def move_mouse(
    __: Event,
    mouse: Optional[Any],
    pointers_sprite_group: Optional[Group] = None,
) -> None:
    if mouse and pointers_sprite_group:
        x, y = mouse.get_pos()
        pointer = pointers_sprite_group.sprites()[0]

        if isinstance(pointer, Pointer):
            pointer.rect.topleft = (x, y)
