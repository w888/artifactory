#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = '1.0'

setup(
    name='artifactory_test',
    version='1.0.1',
    author='SCMRelease.com',
    author_email='support@scmrelease.com',
    packages=['artifactory_test'],
    url='http://scmrelease.com',
    license='LICENSE.txt',
    description='Integration test for Artifactory API python client',
    long_description=open('../README.md').read(),
    install_requires=[
        "nose>=1.0.0",
    ],
)
