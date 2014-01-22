#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup

try:
    long_description = file('README.md').read()
except IOError:
    long_description = ''

setup(
    name='django-dynamic-finder',
    version='0.1',
    url='https://github.com/luanfonceca/django-dynamic-finder',
    license='BSD',
    description='A Django version of the Rails Dynamic Finder, using Django Managers.',
    long_description=long_description,
    author='Luan Fonseca',
    author_email='luanfonceca@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=['django_dynamic_finder'],
    install_requires=['django'],
)