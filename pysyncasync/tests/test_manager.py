from random import randint

import pysyncasync as psa
import pytest

from .common import (
    async_sum,
    sync_sum,
    template,
)


@pytest.fixture(scope="function")
def manager():
    manager = psa.Manager()
    manager.register("sum")(async_sum)
    manager.register("sum")(sync_sum)
    manager.template("template")(template)
    return manager


@pytest.mark.parametrize("a, b, c, d", [
    [randint(0, 100) for _ in range(4)] for _ in range(3)
])
def test_sync(manager, a, b, c, d):
    generated_template = manager.generate("template", psa.SYNC)
    result = generated_template(a, b, c, d)

    assert result == sum((a, b, c, d))


@pytest.mark.parametrize("a, b, c, d", [
    [randint(0, 100) for _ in range(4)] for _ in range(3)
])
@pytest.mark.asyncio
async def test_async(manager, a, b, c, d):
    generated_template = manager.generate("template", psa.ASYNC)
    result = await generated_template(a, b, c, d)

    assert result == sum((a, b, c, d))
