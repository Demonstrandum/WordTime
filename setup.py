#!/usr/bin/python
from setuptools import setup, find_packages
from codecs import open
from os import path

# ======TODO======
# copy bin file(s) to /usr/local/bin/
# ================
# copy PLIST to a new file named
# wordtime.plist in /System/Library/LaunchAgents
# ================

PLIST = '''\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>Demonstrandum.python.script.WordTime</string>
    <key>ProgramArguments</key>
    <array>
        <string>/path/to/python</string>
        <string>/path/to/python/script.py</string>
    </array>
    <key>StandardErrorPath</key>
    <string>/var/log/python_script.error</string>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>
'''

here = path.abspath(path.dirname(__file__))

setup(
    name='WordTime',
    version='0.1',
    description='A macOS menu bar item which tells the time in words.',
    url='https://github.com/Demonstrandum/WordTime',
    author='Demonstrandum',
    author_email='knutsen@jetspace.co',
    license='None',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Anyone',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2',
    ],
    keywords='simple clock words time fuzzy',
    packages=find_packages(),
    install_requires=['rumps', 'pyobjc'],
)
