from typing import Callable, Union, Dict, List
from pygame.event import Event

PENDING_EVENTS: Dict[int, List[Callable]] = {}
EVENTS: Dict[int, List[Callable]] = {}


def event(eventtype: Union[int, "Event"]) -> Callable[[Callable], Callable]:
    def decorator(method: Callable) -> Callable:
        event_type = eventtype if isinstance(eventtype, int) else eventtype.type

        if event_type not in PENDING_EVENTS:
            PENDING_EVENTS[event_type] = []
        PENDING_EVENTS[event_type].append(method)

        return method

    return decorator


def initialize(method_name: Union[str, Callable]) -> None:
    if callable(method_name):
        method_name = method_name.__name__

    for event_type, handlers in PENDING_EVENTS.items():
        for handler in handlers:
            if handler.__name__ == method_name:

                if event_type not in EVENTS:
                    EVENTS[event_type] = []

                EVENTS[event_type].append(handler)
                return

    raise ValueError(f"Handler '{method_name}' not found in pending events.")


def dispatch(event_type: int, evt: Event, *args, **kwargs) -> None:
    if handlers := EVENTS.get(event_type):
        for handler in handlers:
            handler(evt, *args, **kwargs)


def unregister_all() -> None:
    EVENTS.clear()


def unregister_handler(event_type: int, handler: Callable) -> None:
    if event_type in EVENTS:
        EVENTS[event_type].remove(handler)
