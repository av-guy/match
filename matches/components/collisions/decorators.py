from functools import wraps
from typing import Callable, Union

from pygame.sprite import Group, Sprite, spritecollide, groupcollide


def collision(obj1: Union[Sprite, Group], obj2: Group) -> Callable:
    if not isinstance(obj2, Group):
        raise ValueError("obj2 must be a Group")

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            collisions = []

            if isinstance(obj1, Sprite):
                collisions = spritecollide(obj1, obj2, False)
            elif isinstance(obj1, Group):
                group_collisions = groupcollide(obj1, obj2, False, False)
                collisions = [
                    sprite2
                    for sprites in group_collisions.values()
                    for sprite2 in sprites
                ]

            if collisions:
                return func(collisions, *args, **kwargs)

            return lambda *args, **kwargs: None

        return wrapper

    return decorator
