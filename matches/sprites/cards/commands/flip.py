from pygame.event import Event

from ..enums import CardState
from ...events import FLIP_CARD

from ....games import rules
from ....components.events import event
from ..protocols import CardProtocol


@event(FLIP_CARD)
@rules("reveal_rules")
def flip_card(flip_event: Event) -> None:
    card: CardProtocol = flip_event.card

    if card.state is not CardState.REVEALED:
        card.state = CardState.FLIPPING_OVER
