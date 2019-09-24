#!/usr/bin/env python
from setuptools import setup, find_packages
import os, sys

if os.path.exists("VERSION.txt"):
    # this file can be written by CI tools (e.g. Travis)
    with open("VERSION.txt") as version_file:
        version = version_file.read().strip().strip("v")
else:
    version = "0.0.0"

setup(
    name='dataflows-xlsx',
    version=version,
    description='Dataflows support for xlsx files',
    author='Ori Hoch',
    author_email='ori@uumpa.com',
    license='MIT',
    url='https://github.com/OriHoch/dataflows-xlsx',
    packages=find_packages(exclude=["tests", "test.*"]),
    install_requires=['dataflows', 'openpyxl'],
)
