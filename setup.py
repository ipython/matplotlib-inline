#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='matplotlib-inline',
    version='0.1.0',
    description='Inline Matplotlib backend for Jupyter',
    author='IPython Development Team',
    maintainer='IPython Development Team',
    author_email='ipython-dev@scipy.org',
    url='https://github.com/martinRenou/matplotlib-inline',
    license='BSD 3-Clause',
    keywords='python ipython matplotlib jupyter',
    packages=find_packages(exclude=['test']),
    python_requires='>=3.5',
    install_requires=[
        'matplotlib',
        'traitlets',
        'ipython'
    ],
    extras_require={
        'testing': ['flake8'],
    },
    platforms=['any'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
