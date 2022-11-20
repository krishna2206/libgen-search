#!/usr/bin/env python
# -*- coding: utf-8 -*

from __future__ import absolute_import

import os
from codecs import open

from setuptools import find_packages, setup

from libgensearch import __version__
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()


with open('README.md', 'r', encoding='utf-8') as rm_file:
    readme = rm_file.read()

setup(name='libgen-search',
      version=__version__,
      packages=find_packages(exclude=('tests')),
      url='https://github.com/krishna2206/libgen-search',
      long_description_content_type='text/markdown',
      description='Python library for searching books on Libgen.rs',
      long_description=readme,
      author='Fitiavana Anhy Krishna',
      author_email='fitiavana.krishna@gmail.com',
      license='MIT License',
      install_requires=install_requires,
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Topic :: Internet :: WWW/HTTP',
      ])
