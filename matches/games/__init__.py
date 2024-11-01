from typing import Callable, Any
from functools import wraps
from kink import di


def rules(rule_name: str):
    def decorator(method: Callable):
        @wraps(method)
        def wrapper(*args, **kwargs) -> Any:
            rule = di[rule_name]

            if rule(*args, **kwargs):
                return method(*args, **kwargs)

            return lambda *args, **kwargs: None

        return wrapper

    return decorator
