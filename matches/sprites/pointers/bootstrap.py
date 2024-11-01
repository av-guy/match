from typing import Dict
from kink import di
from ...components.graphics.loaders import PygameImageLoader


FILEPATH = di["pointer_graphics_path"]

POINTERS: Dict[str, PygameImageLoader] = {
    "Open": PygameImageLoader(f"{FILEPATH}\\ui_hand_open.png"),
    "Closed": PygameImageLoader(f"{FILEPATH}\\ui_hand_closed.png"),
}


def initialize():
    return POINTERS
