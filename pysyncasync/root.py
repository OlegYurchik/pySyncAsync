from .manager import Manager


def register(*args, **kwargs):
    return manager.register(*args, **kwargs)


def template(*args, **kwargs):
    return manager.template(*args, **kwargs)


def generate(*args, **kwargs):
    return manager.generate(*args, **kwargs)


manager = Manager()
