import inspect
from asyncio import create_task
from typing import Any, Callable, Union

from .base import SUBJECTS
from .enums import Subjects


def check_if_coroutine(func: Callable[..., Any]) -> bool:
    return inspect.iscoroutinefunction(func)


async def call_async_observer(observer: Callable[..., Any], result: Any):
    if isinstance(result, tuple):
        await observer(*result)
    else:
        await observer(result)


def call_sync_observer(observer: Callable[..., Any], result: Any):
    if isinstance(result, tuple):
        observer(*result)
    else:
        observer(result)


async def handle_async_subject(
    func: Callable[..., Any], name: str, *args, **kwargs
) -> None:
    result = await func(*args, **kwargs)

    for observer in SUBJECTS[name]:
        if check_if_coroutine(observer):
            await call_async_observer(observer, result)
        else:
            call_sync_observer(observer, result)


def handle_sync_subject(func: Callable[..., Any], name: str, *args, **kwargs) -> None:
    result = func(*args, **kwargs)

    for observer in SUBJECTS[name]:
        if check_if_coroutine(observer):
            create_task(call_async_observer(observer, result))
        else:
            call_sync_observer(observer, result)


async def handle_async_generator_subject(
    func: Callable[..., Any], name: str, *args, **kwargs
) -> None:
    async for result in func(*args, **kwargs):
        for observer in SUBJECTS[name]:
            if check_if_coroutine(observer):
                await call_async_observer(observer, result)
            else:
                if isinstance(result, tuple):
                    observer(*result)
                else:
                    observer(result)


def handle_sync_generator_subject(
    func: Callable[..., Any], name: str, *args, **kwargs
) -> None:
    for result in func(*args, **kwargs):
        for observer in SUBJECTS[name]:
            if check_if_coroutine(observer):
                create_task(call_async_observer(observer, result))
            else:
                call_sync_observer(observer, result)


def subject(name: Union[str, Subjects]):
    if isinstance(name, Subjects):
        name = name.value

    def decorator(func: Callable[..., Any]):
        if name not in SUBJECTS:
            SUBJECTS[name] = []

        def wrapper(*args, **kwargs):
            if inspect.isasyncgenfunction(func):
                return create_task(
                    handle_async_generator_subject(func, name, *args, **kwargs)
                )

            if check_if_coroutine(func):
                return create_task(handle_async_subject(func, name, *args, **kwargs))

            if inspect.isgeneratorfunction(func):
                return handle_sync_generator_subject(func, name, *args, **kwargs)

            return handle_sync_subject(func, name, *args, **kwargs)

        return wrapper

    return decorator
