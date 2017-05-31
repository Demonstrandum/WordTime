#!/usr/bin/python
from setuptools import setup, find_packages
from codecs import open
from os import path
import os, stat, sys

here = path.abspath(path.dirname(__file__))

setup(
    name='WordTime',
    version='0.1',
    description='A macOS menu bar item which tells the time in words.',
    url='https://github.com/Demonstrandum/WordTime',
    author='Demonstrandum',
    author_email='knutsen@jetspace.co',
    license='GPL-3.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2',
    ],
    keywords='simple clock words time fuzzy',
    packages=find_packages(),
    install_requires=['rumps', 'pyobjc'],
    scripts=['bin/wordtime']
)
