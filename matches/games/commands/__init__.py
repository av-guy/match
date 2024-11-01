from ...components.events import initialize
from .quit import quit_game
from .pygame_gui_events import pygame_gui_button_pressed
from .deal_cards import deal_cards_event_handler


def initialize_handlers() -> None:
    initialize(quit_game)
    initialize(pygame_gui_button_pressed)
    initialize(deal_cards_event_handler)
