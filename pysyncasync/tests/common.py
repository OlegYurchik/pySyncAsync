from pysyncasync import Call


def sync_sum(a, b):
    return a + b


async def async_sum(a, b):
    return a + b


def template(a, b, c, d):
    call1 = Call("sum", a, b)
    yield call1
    call2 = Call("sum", c, d)
    yield call2
    call3 = Call("sum", call1.result, call2.result)
    yield call3
    return call3.result
