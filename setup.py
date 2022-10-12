#! /usr/bin/env python
import numpy
from setuptools import setup, Extension
from Cython.Build import cythonize


extensions = [
    Extension(
        "lsh.cMinhash",
        ["lsh/cMinhash.pyx", "lsh/MurmurHash3.cpp"],
        include_dirs=[numpy.get_include()],
    )
]


setup(
    name="lsh",
    version="0.3.0",
    description="A library for performing shingling and LSH.",
    author="Matti Lyra",
    author_email="matti.lyra@gmail.com",
    url="https://github.com/mattilyra/lsh",
    packages=["lsh"],
    ext_modules=cythonize(extensions),
    install_requires=["numpy"],
    tests_require=[
        "coverage>=4.0.3",
        "pytest>=3.0",
    ],
)
