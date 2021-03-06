#!/usr/bin/env python2

from setuptools import find_packages, setup


setup(
    name='pulp_python_common',
    version='1.1.0a1',
    packages=find_packages(),
    url='http://www.pulpproject.org',
    license='GPLv2+',
    author='Pulp Team',
    author_email='pulp-list@redhat.com',
    description='Common code for Pulp\'s Python support.',
)
