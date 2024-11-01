from typing import Dict
from kink import di
from ...components.graphics.loaders import PygameImageLoader


FILEPATH = di["outline_graphics_path"]

OUTLINES: Dict[str, PygameImageLoader] = {
    "Outline": PygameImageLoader(f"{FILEPATH}\\card_selected_1.png"),
}


def initialize():
    return OUTLINES
