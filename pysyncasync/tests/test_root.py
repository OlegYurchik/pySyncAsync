from random import randint

import pysyncasync as psa
import pytest

from .common import (
    async_sum,
    sync_sum,
    template,
)


def setup_module():
    psa.register("sum")(async_sum)
    psa.register("sum")(sync_sum)
    psa.template("template")(template)


@pytest.mark.parametrize("a, b, c, d", [
    [randint(0, 100) for _ in range(4)] for _ in range(3)
])
def test_sync(a, b, c, d):
    generated_template = psa.generate("template", psa.SYNC)
    result = generated_template(a, b, c, d)

    assert result == sum((a, b, c, d))


@pytest.mark.parametrize("a, b, c, d", [
    [randint(0, 100) for _ in range(4)] for _ in range(3)
])
@pytest.mark.asyncio
async def test_async(a, b, c, d):
    generated_template = psa.generate("template", psa.ASYNC)
    result = await generated_template(a, b, c, d)

    assert result == sum((a, b, c, d))
