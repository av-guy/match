from typing import Optional, Union
from pygame import Surface, image


class PygameImageLoader:
    def __init__(self, path: str):
        self._path = path
        self._image: Union[Surface, None] = None

    def load(self, path: Optional[str] = None) -> Surface:
        if not path:
            path = self._path

        if not self._image:
            self._image = image.load(path).convert_alpha()

        return self._image
