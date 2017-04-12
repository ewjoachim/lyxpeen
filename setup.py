#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

VERSION = '0.0.0'
INSTALL_REQUIRES = [
    "django",
    "psycopg2",
    "djangorestframework",
    "markdown",
    "django-filter",
]

setup(
    name='lyxpeen',
    version=VERSION,
    description="A modern choir management website",
    long_description="",
    author='Joachim Jablon',
    author_email='ewjoachim@gmail.com',
    url='https://github.com/ewjoachim/lyxpeen',
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    license="MIT",
    entry_points={
        'console_scripts': ['lyxpeen=lyxpeen.project.manage:main'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Artistic Software',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: JavaScript',
    ],
)
