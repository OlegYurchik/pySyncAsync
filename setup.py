from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name="pySyncAsync",
    version="1.0.0",
    url="https://github.com/OlegYurchik/pySyncAsync",

    description="",
    long_description=open(join(dirname(__file__), "README.md")).read(),
    long_description_content_type="text/markdown",

    author="Oleg Yurchik",
    author_email="oleg.yurchik@protonmail.com",

    packages=find_packages(),
    tests_require=["pytest", "pytest-asyncio"],
    test_suite="pysyncasync.tests",
)
