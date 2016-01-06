#!/usr/bin/python3

__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-08-04 15:28:03$"

from setuptools import setup

setup (
    name='KPIR API',
    version='0.1',
    packages=['kpir','kpir.core'],
    package_dir={'': 'src'},
    install_requires=[
        'Flask>=0.10',
        'Flask-SQLAlchemy>=1.0',
        'Flask-Testing>=0.4',
        'SQLAlchemy>=0.8'
    ],

    author='Dawid Pych',
    author_email='dawidpych@gmailcom',

    summary='Just another Python package for the cheese shop',
    
    url='http://projectweb.ovh/',
    license='',
    description='',
    long_description='Long description of the package',
    
    data_files=[
        ('/opt/kpir',['src/config.ini','src/run.py','src/db_create.py','src/db_migrate.py'])
    ]
# could also include long_description, download_url, classifiers, etc.  
)