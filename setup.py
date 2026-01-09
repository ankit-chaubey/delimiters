#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="delimiters",
    version="0.1.0",

    author="Ankit Chaubey",
    author_email="m.ankitchaubey@gmail.com",

    description="Advanced formatting add-ons for Telethon with predictable Markdown and HTML parsing",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/ankit-chaubey/delimiters",

    packages=find_packages(include=["delimiters", "delimiters.*"]),

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],

    install_requires=[
        "telethon>=1.34.0",
    ],

    python_requires=">=3.9",

    keywords=[
        "telegram",
        "telethon",
        "markdown",
        "html",
        "parser",
        "entities",
        "formatting",
        "delimiters",
    ],

    project_urls={
        "Source": "https://github.com/ankit-chaubey/delimiters",
        "Bug Tracker": "https://github.com/ankit-chaubey/delimiters/issues",
        "Documentation": "https://github.com/ankit-chaubey/delimiters#readme",
    },
)
