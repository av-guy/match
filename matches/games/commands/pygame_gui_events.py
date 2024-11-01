from typing import Any

from pygame.event import Event
from pygame_gui import UI_BUTTON_PRESSED

from kink import inject

from ...components.events import event

from ...sprites.events import RESET_GAME
from ...sprites.menus.buttons.enums import ButtonType


@event(UI_BUTTON_PRESSED)
@inject()
def pygame_gui_button_pressed(btn_press_event: Event, events: Any) -> None:
    if btn_press_event.ui_element.button_type == ButtonType.RESET_GAME:
        events.post(RESET_GAME)
