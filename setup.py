#!/usr/bin/env python

__version__ = "1.5"

from setuptools import setup, find_packages


setup(
    name="terra_colab",
    version=__version__,
    packages=find_packages(),
    long_description=open("README.rst").read(),
    install_requires=[
        "GitPython==3.1.24",
        "python-dotenv==0.19.2",
    ],
)
