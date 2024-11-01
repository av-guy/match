# pylint: disable=no-name-in-module

from math import cos, radians
from typing import Dict, Optional
from pygame import transform
from pygame.surface import Surface

from kink import inject

from ..enums import CardRank, CardSuit, CardState
from ..protocols import CardProtocol

from ....components.graphics.loaders import ImageLoader

FLIP_SPEED = 500


def calculate_visibility(t: float) -> float:
    return round(abs(cos(radians(t % 360))), 2)


def keep_card_centered(card: CardProtocol, graphic: Surface) -> Surface:
    x, _ = card.position

    visibility = calculate_visibility(card.angle)
    card_width = int(card.width * visibility)

    graphic = transform.scale(graphic, (card_width, 100))
    card.rect.x = int(x + (card.width - card_width) / 2)

    return graphic


@inject()
def render(
    card: CardProtocol,
    delta: float,
    card_back: Optional[ImageLoader] = None,
    card_graphics: Optional[Dict[CardSuit, Dict[CardRank, ImageLoader]]] = None,
) -> None:
    if card_back and card_graphics:

        if card.state is CardState.FLIPPING_OVER:
            card.angle += delta * FLIP_SPEED

            if card.angle >= 180:
                card.angle = 180
                card.state = CardState.REVEALED

        if card.state is CardState.FLIPPING_BACK:
            card.angle += delta * FLIP_SPEED

            if 0 <= card.angle <= 180:
                card.angle = 0
                card.state = CardState.HIDDEN

        if card.state in (CardState.FLIPPING_BACK, CardState.FLIPPING_OVER):
            if 90 < card.angle < 270:
                graphic = card_graphics[card.suit][card.rank].load()
            else:
                graphic = card_back.load()

            graphic = keep_card_centered(card, graphic)

        if card.state is CardState.REVEALED:
            graphic = card_graphics[card.suit][card.rank].load()

        if card.state is CardState.HIDDEN:
            graphic = card_back.load()

        card.image = graphic
