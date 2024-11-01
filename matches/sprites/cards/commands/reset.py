from pygame.event import Event
from pygame.time import set_timer

from ..enums import CardState
from ...events import RESET_CARD


from ....components.events import event
from ....games.events import DEAL_CARDS
from ..protocols import CardProtocol


@event(RESET_CARD)
def reset_card(flip_event: Event) -> None:
    card: CardProtocol = flip_event.card

    try:
        if flip_event.last is True:
            set_timer(DEAL_CARDS, 2000, loops=1)
    except AttributeError:
        pass

    if card.state is not CardState.HIDDEN:
        card.state = CardState.FLIPPING_BACK
