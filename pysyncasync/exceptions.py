class PSAException(Exception):
    pass


class PSARegisterIncorrectCallbackException(PSAException):
    def __init__(self):
        super().__init__(
            "Cannot register callback: incorrect callback. Callback must be coroutine function or "
            "just function."
        )


class PSADecorateIncorrectCallbackException(PSAException):
    def __init__(self):
        super().__init__(
            "Cannot decorate callback: incorrect callback. Callback must be async generator or "
            "just generator."
        )
