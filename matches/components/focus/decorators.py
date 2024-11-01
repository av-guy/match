from enum import Enum
from functools import wraps
from kink import di


def focus(required_focus_area: str | Enum):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if di["focus_area"] == required_focus_area:
                return func(*args, **kwargs)
            return None

        return wrapper

    return decorator
