#!/usr/env/bin python
#-*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="xmind",
    version="0.0.1",
    packages=find_packages(),

    install_requires=["distribute"],

    author="Michel Kern",
    author_email="echopraxium@yahoo.com",
    description="A fork of XMind python SDK with extensions for import / export (e.g. Graphviz)",
    license="MIT",
    keywords="XMind, SDK, mind mapping, extension, import, export, graphviz",
    url="https://github.com/Almerxsese/xmind-sdk-python"
)
