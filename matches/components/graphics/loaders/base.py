from typing import Protocol, TypeVar, Optional

T_co = TypeVar("T_co", covariant=True)


class ImageLoader(Protocol[T_co]):
    def load(self, path: Optional[str] = None) -> T_co: ...
