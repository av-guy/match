from typing import Any, Callable, Union, List
from .base import SUBJECTS
from .enums import Subjects


def observer(names: Union[str, Subjects, List[Union[str, Subjects]]]):
    if not isinstance(names, list):
        names = [names]

    names = [name.value if isinstance(name, Subjects) else name for name in names]

    def decorator(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        for name in names:
            if name not in SUBJECTS:
                SUBJECTS[name] = []
            SUBJECTS[name].append(func)

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator
