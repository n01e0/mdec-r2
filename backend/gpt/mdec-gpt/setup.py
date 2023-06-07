#!/usr/bin/env python3
from setuptools import setup

__version__ = '0.0.1'

setup(name='mdec-gpt',
      version=__version__,
      description='mdec-gpt',
      packages=['mdecgpt'],
      install_requires=['mdec-base', 'openai'],
      python_requires='>=3.8'
    )
