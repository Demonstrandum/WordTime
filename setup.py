#!/usr/bin/python
from setuptools import setup, find_packages
from codecs import open
from os import path
import os, stat

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

binName = 'tmpwordtimebin'

binCont = '''\
#!/usr/local/bin/python
from wordtime import menubar
menubar.main()
'''

print("Making and writing to bin file '" + binName + "'...\n")
binFile = open(binName, 'w')
binFile.write(binCont)
binFile.close()

print("Making file executable...\n")
binStat = os.stat(binName)
os.chmod(binName, binStat.st_mode | stat.S_IEXEC)

binNewPath = '/usr/local/bin/wordtime'
print("Moving bin file to bin directory with name: " + binNewPath + "'...\n")
os.rename(binName, binNewPath)
