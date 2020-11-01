import pysyncasync as psa


def test_import():
    names = {
        "generate",
        "register",
        "template",
        "Call",
        "Manager",
        "ASYNC",
        "SYNC",
    }
    assert names <= set(dir(psa))
