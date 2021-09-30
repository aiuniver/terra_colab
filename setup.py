#!/usr/bin/env python

__version__ = "1.1"

from setuptools import setup, find_packages


setup(
    name="terra_colab",
    version=__version__,
    packages=find_packages(),
    long_description=open("README.rst").read(),
    install_requires=[
        "requests~=2.23.0",
        "GitPython==3.1.18",
        "python-dotenv==0.19.0",
        "tensorflow==2.6.0",
        "Django==3.2.6",
    ],
    entry_points={
        "console_scripts": [
            "tc-web = terra_colab.commands:web",
        ]
    },
)
