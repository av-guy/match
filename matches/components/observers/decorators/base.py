from typing import Any, Callable, Dict, List, Union, Awaitable

SyncOrAsyncCallable = Callable[[Any], Union[Awaitable[Any], Any]]
SUBJECTS: Dict[str, List[SyncOrAsyncCallable]] = {}
