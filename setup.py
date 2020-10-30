from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name="pySyncAsync",
    version="0.0.1",
    author="Oleg Yurchik",
    author_email="oleg.yurchik@protonmail.com",
    url="https://github.com/OlegYurchik/pySyncAsync",
    description="",
    long_description=open(join(dirname(__file__), "README.md")).read(),
    packages=find_packages(exclude=["tests"]),
    tests_require=["pytest", "pytest-asyncio", "pytest-random-order"],
    test_suite="tests",
)
