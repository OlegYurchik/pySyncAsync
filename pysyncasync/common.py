import inspect

from .exceptions import (
    PSADecorateIncorrectCallbackException,
    PSARegisterIncorrectCallbackException,
)


class Manager:
    def __init__(self):
        self._callables = {}

    def register(self, callback):
        if inspect.iscoroutinefunction(callback):
            self._callables[f"{callback.__name__}:async"] = callback
        elif callable(callback):
            self._callables[f"{callback.__name__}:sync"] = callback
        else:
            raise PSARegisterIncorrectCallbackException()
        return callback

    def decorator(self, callback):
        if inspect.isasyncgenfunction(callback):
            return self._async_decorator(callback)
        elif inspect.isgeneratorfunction(callback):
            return self._sync_decorator(callback)
        else:
            raise PSADecorateIncorrectCallbackException()

    def _sync_decorator(self, callback):
        def wrapper(*args, **kwargs):
            pass
        return wrapper

    def _async_decorator(self, callback):
        async def wrapper(*args, **kwargs):
            pass
        return wrapper
