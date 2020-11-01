import inspect

from .call import Call
from .constants import ASYNC, SYNC
from .exceptions import (
    PSADecorateIncorrectTemplateException,
    PSAExecuteIncorrectCallException,
    PSAExecuteIncorrectCallbackNameException,
    PSAGenerateIncorrectMethodException,
    PSAGenerateIncorrectTemplateException,
    PSARegisterIncorrectCallbackException,
)
from .generator import Generator


class Manager:
    def __init__(self):
        self._callbacks = {}
        self._templates = {}

    def clear(self):
        self._callbacks.clear()
        self._templates.clear()

    def register(self, name=None):
        def decorator(callback):
            callback_name = callback.__name__ if name is None else name
            if inspect.iscoroutinefunction(callback):
                self._callbacks[f"{callback_name}:{ASYNC}"] = callback
            elif callable(callback):
                self._callbacks[f"{callback_name}:{SYNC}"] = callback
            else:
                raise PSARegisterIncorrectCallbackException()
            return callback
        return decorator

    def template(self, name=None):
        def decorator(callback):
            if not inspect.isgeneratorfunction(callback):
                raise PSADecorateIncorrectTemplateException()
            template_name = callback.__name__ if name is None else name
            self._templates[template_name] = callback
            return callback
        return decorator

    def generate(self, template, method):
        if isinstance(template, str):
            template = self._templates.get(template)
        elif not inspect.isgeneratorfunction(template):
            raise PSAGenerateIncorrectTemplateException(template)
        if method == SYNC:
            return self._sync_generate(template)
        elif method == ASYNC:
            return self._async_generate(template)
        else:
            raise PSAGenerateIncorrectMethodException()

    def _sync_generate(self, template):
        def wrapper(*args, **kwargs):
            generator = Generator(generator=template(*args, **kwargs))
            for call in generator:
                if not isinstance(call, Call):
                    raise PSAExecuteIncorrectCallException()
                callback = self._callbacks.get(f"{call.name}:{SYNC}")
                if callback is None:
                    raise PSAExecuteIncorrectCallbackNameException(name=call.name)
                call.result = callback(*call.args, **call.kwargs)
            return generator.result
        return wrapper

    def _async_generate(self, template):
        async def wrapper(*args, **kwargs):
            generator = Generator(generator=template(*args, **kwargs))
            for call in generator:
                if not isinstance(call, Call):
                    raise PSAExecuteIncorrectCallException()
                callback = self._callbacks.get(f"{call.name}:{ASYNC}")
                if callback is None:
                    raise PSAExecuteIncorrectCallbackNameException(name=call.name)
                call.result = await callback(*call.args, **call.kwargs)
            return generator.result
        return wrapper
