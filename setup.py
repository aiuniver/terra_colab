#!/usr/bin/env python3

from setuptools import setup, find_packages
from os.path import join, dirname
from terra_colab import __version__


setup(
    name="terra_colab",
    version=__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), "README.md")).read(),
    install_requires=["dill>=0.3.3", "requests~=2.23.0", "datascience>=0.10.6"],
    # entry_points={"console_scripts": ["terra_colab_web = terra_colab.commands:web"]},
    scripts=["scripts/terra_colab_web"],
)
