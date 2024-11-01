from pygame.event import Event, custom_type

FLIP_CARD_TYPE = custom_type()
FLIP_CARD = Event(FLIP_CARD_TYPE, {"card": None, "player_origin": True})
