#!/usr/bin/env python3

__version__ = "1.0"

from setuptools import setup, find_packages


setup(
    name="terra_colab",
    version=__version__,
    packages=find_packages(),
    long_description=open("README.rst").read(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "tc-init = terra_colab.commands:init",
        ]
    },
)
