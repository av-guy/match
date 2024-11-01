from typing import Dict, Optional

from pygame.sprite import Sprite, Group
from kink import inject

from ...components.graphics.loaders import ImageLoader


@inject
class Pointer(Sprite):
    def __init__(
        self,
        pointer_graphics: Optional[Dict[str, ImageLoader]] = None,
        pointers_sprite_group: Optional[Group] = None,
    ) -> None:
        super().__init__()

        if pointer_graphics is not None:
            self.image = pointer_graphics["Open"].load()
            self.rect = self.image.get_rect()
            self.rect.topleft = (100, 100)
        else:
            raise ValueError("Pointer graphics must be provided")

        if pointers_sprite_group is not None:
            pointers_sprite_group.add(self)
