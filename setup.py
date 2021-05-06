#!/usr/bin/env python3

from setuptools import setup, find_packages
from terra_colab import __version__


setup(
    name="terra_colab",
    version=__version__,
    packages=find_packages(),
    long_description=open("README.rst").read(),
    install_requires=[
        "dill>=0.3.3",
        "requests~=2.23.0",
        "folium==0.2.1",
        "pymorphy2>=0.9.1",
    ],
    entry_points={
        "console_scripts": [
            "tc-auth = terra_colab.commands:auth",
            "tc-gdmount = terra_colab.commands:gdmount",
            "tc-dataset = terra_colab.commands:dataset",
        ]
    },
    scripts=[
        "scripts/tc-init",
        "scripts/tc-web",
    ],
)
