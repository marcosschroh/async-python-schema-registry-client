#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" setup.py for python-schema_registry."""

from setuptools import find_packages, setup

__version__ = "1.0.0"

with open("README.md") as readme_file:
    long_description = readme_file.read()

requires = ["fastavro", "httpx", "aiofiles"]
description = f"Asyn Python Rest Client to interact against Schema Registry Confluent Server" f"to manage Avro Schemas"

setup(
    name="async-python-schema-registry-client",
    version=__version__,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Marcos Schroh",
    author_email="schrohm@gmail.com",
    install_requires=requires,
    url="https://github.com/marcosschroh/async-python-schema-registry-client",
    download_url="https://pypi.org/project/async-python-schema-registry-client",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development",
    ],
    keywords=(
        """
        Schema Registry, Python, Async, Avro, Apache, Apache Avro
        """
    ),
)
