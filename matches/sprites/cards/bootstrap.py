from typing import Dict, Union, Literal
from kink import di

from .enums import CardSuit, CardRank, CardBack
from ...components.graphics.loaders import PygameImageLoader

FACES = ["J", "Q", "K", "A"]
FILEPATH = di["card_graphics_path"]

RankTypes = Dict[CardRank, PygameImageLoader]
BackTypes = Dict[CardBack, PygameImageLoader]
CardTypes = Union[RankTypes, BackTypes]

Backs = Literal["Backs"]

CARDS: Dict[Union[CardSuit, Backs], CardTypes] = {}


def suit_factory(suit: CardSuit) -> RankTypes:
    suits = {
        CardSuit.HEARTS: "hearts",
        CardSuit.DIAMONDS: "diamonds",
        CardSuit.CLUBS: "clubs",
        CardSuit.SPADES: "spades",
    }

    suit_folder = suits[suit]
    suit_color = "black"

    if suit in (CardSuit.HEARTS, CardSuit.DIAMONDS):
        suit_color = "red"

    full_path = f"{FILEPATH}\\{suit_folder}\\{suit_color}"

    num_rank = [
        CardRank.TWO,
        CardRank.THREE,
        CardRank.FOUR,
        CardRank.FIVE,
        CardRank.SIX,
        CardRank.SEVEN,
        CardRank.EIGHT,
        CardRank.NINE,
        CardRank.TEN,
    ]

    nums = [PygameImageLoader(f"{full_path}\\{i}.png") for i in range(1, 11)]
    card_dict = {rank: nums[i] for i, rank in enumerate(num_rank, start=1)}

    card_dict.update(
        {
            CardRank.JACK: PygameImageLoader(f"{full_path}\\J.png"),
            CardRank.QUEEN: PygameImageLoader(f"{full_path}\\Q.png"),
            CardRank.KING: PygameImageLoader(f"{full_path}\\K.png"),
            CardRank.ACE: PygameImageLoader(f"{full_path}\\A.png"),
        }
    )

    return card_dict


def back_factory() -> BackTypes:
    backs = [
        CardBack.BACK_1,
        CardBack.BACK_2,
        CardBack.BACK_3,
        CardBack.BACK_4,
        CardBack.BACK_5,
        CardBack.BACK_6,
        CardBack.BACK_7,
        CardBack.BACK_8,
    ]

    back_dict = {
        back: PygameImageLoader(f"{FILEPATH}\\backs\\{index}.png")
        for index, back in enumerate(backs, start=1)
    }

    return back_dict


def initialize() -> Dict[Union[CardSuit, Backs], CardTypes]:
    if not CARDS:
        CARDS.update({suit: suit_factory(suit) for suit in CardSuit})
        CARDS.update({"Backs": back_factory()})
    return CARDS
