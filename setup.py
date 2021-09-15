#!/usr/bin/env python

__version__ = "1.0"

from setuptools import setup, find_packages


setup(
    name="terra_colab",
    version=__version__,
    packages=find_packages(),
    long_description=open("README.rst").read(),
    install_requires=[
        "requests~=2.23.0",
        "GitPython==3.1.18",
    ],
    entry_points={
        "console_scripts": [
            "tc-web = terra_colab.commands:web",
        ]
    },
)
