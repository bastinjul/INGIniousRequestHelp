#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import inginious_request_help

setup(
    name="inginious_request_help",
    version=inginious_request_help.__version__,
    description="Plugin to request help for a specific task to administration team of a course",
    packages=find_packages(),
    install_requires=["inginious>=0.5.dev0"],
    tests_require=[],
    extras_require={},
    scripts=[],
    include_package_data=True,
    author="The INGInious authors",
    author_email="inginious@info.ucl.ac.be",
    license="AGPL 3",
    url="https://github.com/bastinjul/INGIniousRequestHelp"
)
