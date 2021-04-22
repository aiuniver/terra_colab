#!/usr/bin/env python3

from setuptools import setup, find_packages
from os.path import join, dirname
from terra_colab import __version__


setup(
    name="terra_colab",
    version=__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), "README.md")).read(),
    entry_points={
        "console_scripts": ["terra_colab_web_launch = terra_colab.commands:getup"]
    },
)
