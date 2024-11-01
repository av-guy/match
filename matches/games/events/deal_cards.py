from pygame.event import Event, custom_type

DEAL_CARDS_TYPE = custom_type()
DEAL_CARDS = Event(DEAL_CARDS_TYPE, {"card": None, "player_origin": True})
