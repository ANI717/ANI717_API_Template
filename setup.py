#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Revision History:
    Animesh Bala Ani: Baseline Script.

"""

import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fp:
    requirements = fp.read().split('\n')


setuptools.setup(
    name="ani717-api-template",
    version="0.0.1",
    author="Animesh Bala Ani",
    author_email="animesh.ani@live.com",
    description="A Python Fast API Template for Machine Learning Applications to Receive HTTP POST Request and Respond Accordingly.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ANI717/ANI717_API_Template",
    project_urls={
        "Bug Tracker": "https://github.com/ANI717/ANI717_API_Template/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9.7",
    install_requires=requirements,
)
