#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name='WordTime',
    version='1.0',
    description='A macOS menu bar item which tells the time in words.',
    url='https://github.com/Demonstrandum/WordTime',
    author='Demonstrandum',
    author_email='knutsen@jetspace.co',
    license='GPL-3.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2',
    ],
    keywords='simple clock words time fuzzy',
    packages=find_packages(),
    install_requires=['rumps', 'pyobjc'],
    scripts=['bin/wordtime']
)

autostart = str(raw_input("\nWould you like to enable now and on login? [y/n] ")).upper()

if autostart == "Y" or autostart == "YES":
    import autorun
