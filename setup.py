#!/usr/bin/python3
import os
import sys
from setuptools import setup

data_dir = os.path.dirname(os.path.realpath(__file__))

print(data_dir)
print(os.path.join(sys.prefix,'opt','kpir'))

setup(
    name='KPIR API',
    version='0.1',
    packages=['kpir', 'kpir.core'],
    package_dir={'': 'src'},
    url='',
    license='',
    author='Dawid Pych',
    author_email='dawidpych@gmail.com',
    description='',
    install_requires=['flask'],
    data_files=[
        ('opt',[os.path.join(data_dir, '/src/test.txt')])
    ]
)
