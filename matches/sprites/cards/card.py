from typing import Dict, TypeVar, Optional, Tuple
from dataclasses import dataclass

from pygame.sprite import Sprite, Group
from kink import inject

from .enums import CardRank, CardSuit, CardState
from .models import CardData

from ...components.graphics.loaders import ImageLoader
from .graphics import render_card_graphics

T = TypeVar("T")
K = Dict[CardSuit, Dict[CardRank, ImageLoader]]


@dataclass
class CardAttributes:
    suit: CardSuit
    rank: CardRank
    state: CardState = CardState.HIDDEN


@dataclass
class CardPosition:
    angle: float = 0.0
    position: Tuple[int, int] = (0, 0)


@inject
class Card(Sprite):
    def __init__(
        self,
        data: CardData,
        card_graphics: Optional[K] = None,
        cards_sprite_group: Optional[Group] = None,
    ) -> None:
        super().__init__()
        self.attributes = CardAttributes(suit=data.suit, rank=data.rank)
        self.position_data = CardPosition(position=(data.x, data.y))

        if card_graphics is not None:
            self.image = card_graphics[data.suit][data.rank].load()

            if self.image:
                self.rect = self.image.get_rect(center=(data.x, data.y))
                self.rect.topleft = (data.x, data.y)
                self._width = self.image.get_width()
            else:
                raise ValueError("Failed to load card image")
        else:
            raise ValueError("`card_graphics` is required")

        if cards_sprite_group is not None:
            cards_sprite_group.add(self)

    @property
    def angle(self) -> float:
        return int(self.position_data.angle)

    @angle.setter
    def angle(self, value: float) -> None:
        self.position_data.angle = int(value % 360)

    @property
    def width(self) -> int:
        return self._width

    @property
    def position(self) -> Tuple[int, int]:
        return self.position_data.position

    @property
    def data(self) -> CardData:
        x, y = self.rect.topleft if self.rect else (0, 0)
        return CardData(self.attributes.suit, self.attributes.rank, int(x), int(y))

    @property
    def state(self) -> CardState:
        return self.attributes.state

    @state.setter
    def state(self, value: CardState) -> None:
        self.attributes.state = value

    @property
    def suit(self) -> CardSuit:
        return self.attributes.suit

    @property
    def rank(self) -> CardRank:
        return self.attributes.rank

    def update(self, *args, **kwargs) -> None:
        delta = args[0]
        render_card_graphics(self, delta)
        super().update(*args, **kwargs)
