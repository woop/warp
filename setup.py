#!/usr/bin/env python

from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='warp',
    description='WARP: Wrapper around Replicated Processes',
    author='Willem Pienaar',
    license="Apache-2.0",
    author_email='pypi-warp@willem.co',
    url='https://github.com/woop/warp',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
