#!/usr/bin/env python
# encoding: utf-8


"""PyShim, an experiment in LD_PRELOAD shimming with Python."""


from setuptools import setup, find_packages
from Cython.Distutils import build_ext
from distutils.extension import Extension


__version__ = "0.1.1"
README = open("README.rst").read()
REQUIREMENTS = open("requirements.txt").readlines()


setup(
    name="pyshim",
    version=__version__,
    description=__doc__,
    long_description=README,
    author="Craig J Perry",
    author_email="craigp84@gmail.com",
    install_requires=REQUIREMENTS,
    packages=find_packages(exclude=["tests"]),
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("pyshim.pyshim", ["pyshim/pyshim.pyx"])]
)

