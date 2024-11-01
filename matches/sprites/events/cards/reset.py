from pygame.event import Event, custom_type

RESET_CARD_TYPE = custom_type()
RESET_CARD = Event(RESET_CARD_TYPE, {"card": None})
