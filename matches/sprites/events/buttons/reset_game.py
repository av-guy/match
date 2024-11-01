from pygame.event import Event, custom_type

RESET_GAME_TYPE = custom_type()
RESET_GAME = Event(RESET_GAME_TYPE, {"card": None, "player_origin": True})
