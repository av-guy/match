from typing import Optional

from pygame.sprite import Group
from pygame_gui import elements, UIManager

from kink import inject

from .enums import ButtonType


@inject
class GameButton(elements.UIButton):
    def __init__(
        self,
        *args,
        ui_manager: Optional[UIManager] = None,
        buttons_sprite_group: Optional[Group] = None,
        button_type: Optional[ButtonType] = None,
        **kwargs
    ):
        kwargs["manager"] = ui_manager

        if button_type is None:
            raise ValueError("Button type is required")

        self._button_type = button_type

        super().__init__(*args, **kwargs)

        if buttons_sprite_group is not None:
            buttons_sprite_group.add(self)

    @property
    def button_type(self) -> Optional[ButtonType]:
        return self._button_type
