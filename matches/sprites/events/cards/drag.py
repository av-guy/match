from pygame.event import Event, custom_type

DRAG_CARD_TYPE = custom_type()
DRAG_CARD = Event(DRAG_CARD_TYPE, {"card": None, "player_origin": True})
