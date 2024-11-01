# pylint: disable=unused-import

from . import bootstrap
from .game_loop import GameLoop


if __name__ == "__main__":
    game_loop = GameLoop()
    game_loop.run()
