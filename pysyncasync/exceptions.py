from .constants import METHODS


class PSAException(Exception):
    pass


class PSADecorateException(PSAException):
    def __init__(self, reason):
        super().__init__(f"Cannot decorate template: {reason}")


class PSAExecuteException(PSAException):
    def __init__(self, reason):
        super().__init__(f"Cannot continue execution template: {reason}")


class PSAGenerateException(PSAException):
    def __init__(self, reason):
        super().__init__(f"Cannot generate template: {reason}")


class PSARegisterException(PSAException):
    def __init__(self, reason):
        super().__init__(f"Cannot register callback: {reason}")


class PSADecorateIncorrectTemplateException(PSADecorateException):
    def __init__(self):
        super().__init__("incorrect template. Template must be generator function.")


class PSAExecuteIncorrectCallException(PSAExecuteException):
    def __init__(self):
        super().__init__("incorrect call object. Call object must be Call type.")


class PSAExecuteIncorrectCallbackNameException(PSAExecuteException):
    def __init__(self, name):
        super().__init__(f"incorrect callback name. Manager has no callback with name '{name}'.")


class PSAGenerateIncorrectMethodException(PSAGenerateException):
    def __init__(self):
        super().__init__(f"incorrect method. Method must be one from {tuple(METHODS)}.")


class PSAGenerateIncorrectTemplateException(PSAGenerateException):
    def __init__(self, template):
        super().__init__(
            f"incorrect template. Template must be str or generator function, not {type(template)}",
        )


class PSARegisterIncorrectCallbackException(PSARegisterException):
    def __init__(self):
        super().__init__(
            "incorrect callback. Callback must be coroutine function or just function."
        )
