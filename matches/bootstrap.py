# pylint: disable=unused-import

from .games.core import config
from .games.match.screens import initialize as match_initialize
from .games.match.focuses import focus_game_board

match_initialize(5, 4)
focus_game_board()
