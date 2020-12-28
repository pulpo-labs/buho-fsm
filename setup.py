import os
from setuptools import setup, find_namespace_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='buho-fsm',
    version='0.1.0',
    packages=find_namespace_packages(include=['buho.*']),
    include_package_data=True,
    description='This project contains the basic elements for statemachine usage.',
    long_description=README,
    url='git@github.com:pulpo-labs/buho-fsm.git',
    author='Ricardo Santos',
    author_email='ricardo.santos.diaz@gmail.com',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        "Django >= 3.0.0",
        "django-fsm >= 2.7.0",
    ]
)
