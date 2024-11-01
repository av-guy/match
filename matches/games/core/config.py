# pylint: disable=unused-import
# pylint: disable=wrong-import-position
# pylint: disable=no-name-in-module

from typing import Dict, Any
from os import getcwd
from kink import di

from pygame.sprite import Group
from pygame import display, time, init, mouse, event
from pygame_gui import UIManager

CARD_GRAPHICS_PATH = f"{getcwd()}\\matches\\assets\\img\\deck_of_cards"
POINTER_GRAPHICS_PATH = f"{getcwd()}\\matches\\assets\\img\\mouse_pointers"
OUTLINE_GRAPHICS_PATH = f"{getcwd()}\\matches\\assets\\img\\outlines"
PYGAME_GUI_THEMES_PATH = f"{getcwd()}\\matches\\sprites\\menus\\themes\\styles.json"

di["card_graphics_path"] = CARD_GRAPHICS_PATH
di["pointer_graphics_path"] = POINTER_GRAPHICS_PATH
di["outline_graphics_path"] = OUTLINE_GRAPHICS_PATH
di["pygame_gui_themes_path"] = PYGAME_GUI_THEMES_PATH

from ..commands import initialize_handlers as initialize_global_commands

initialize_global_commands()

from ...sprites.cards.bootstrap import initialize as cards_initialize
from ...sprites.cards.enums import CardBack

from ...sprites.pointers.bootstrap import initialize as pointer_initialize
from ...sprites.pointers.pointer import Pointer

from ...sprites.outlines.bootstrap import initialize as outline_initialize


CONFIG: Dict[str, Any] = {
    "screen_width": 1024,
    "screen_height": 768,
    "groups": {
        "cards": Group(),
        "decks": Group(),
        "outlines": Group(),
        "buttons": Group(),
        "pointers": Group(),
    },
    "graphics": {
        "card": cards_initialize(),
        "pointer": pointer_initialize(),
        "outline": outline_initialize(),
    },
}

display.set_caption("Match 2 Game")

di["screen"] = display.set_mode((CONFIG["screen_width"], CONFIG["screen_height"]))
di["clock"] = time.Clock()

di["card_back"] = CONFIG["graphics"]["card"]["Backs"][CardBack.BACK_2]

di["collisions"] = []

di["groups"] = list(CONFIG["groups"].values())

di["screen_width"] = CONFIG["screen_width"]
di["screen_height"] = CONFIG["screen_height"]

for key, value in CONFIG["graphics"].items():
    di[f"{key}_graphics"] = value

for key, value in CONFIG["groups"].items():
    di[f"{key}_sprite_group"] = value

init()

Pointer()

di["mouse"] = mouse
di["events"] = event
di["display"] = display

di["ui_manager"] = UIManager(
    (di["screen_width"], di["screen_height"]),
    theme_path=PYGAME_GUI_THEMES_PATH
)

mouse.set_visible(False)
