# pySyncAsync

A library for template generation of synchronous and asynchronous functions in Python.

* [Release Notes](#release-notes)
* * [Version 0.0.1](#version-0.0.1)
* * [Version 1.0.0](#version-1.0.0)
* [Installation](#installation)
* [Quick start](#quick-start)
* [User guide](#user-guide)
* * [Manager](#manager)
* * [Root manager](#root-manager)
* * [Call object](#call-object)
* * [Template function](#template-function)
* [Examples](#Examples)

## Release Notes

### Version 0.0.1

Doesn't work, only library base

### Version 1.0.0

* Add README
* Add Manager class
* Add root manager
* Add tests for import, common manager and root manager

## Installation

You can install this library by download from GitHub:

```shell script
git clone https://github.com/OlegYurchik/pySyncAsync
cd pySyncAsync
python setup.py install
```

or install from PyPI:

```shell script
pip install pySyncAsync
```

## Quick start

Just let me show simple code for set your templates and run them

```python
import asyncio
import time
from random import randint

import pysyncasync as psa


@psa.register("sum")
def sync_func(a, b):
    print("SUM SYNC START")
    time.sleep(1)
    return a + b


@psa.register("sum")
async def async_func(a, b):
    print("SUM ASYNC START")
    await asyncio.sleep(1)
    return a + b


def worker():
    a, b, c, d = (randint(0, 10**9) for _ in range(4))

    call1 = psa.Call("sum", a, b)
    yield call1

    call2 = psa.Call("sum", c, d)
    yield call2

    call3 = psa.Call("sum", call1.result, call2.result)
    yield call3

    return call3.result


def main():
    generated_worker = psa.generate(worker, psa.SYNC)
    return generated_worker()


def a_main():
    generated_worker = psa.generate(worker, psa.ASYNC)    
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(generated_worker())


if __name__ == "__main__":
    print("SYNC SESSION")    
    main()
    print("ASYNC SESSION")
    a_main()
```

## User guide

### Manager

### Root manager

### Call object

### Template function

## Examples
