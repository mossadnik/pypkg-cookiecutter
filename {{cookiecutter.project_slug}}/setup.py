#!/usr/bin/env python

from setuptools import setup, find_packages

def _read(fname):
    try:
        with open(fname) as fobj:
            return fobj.read()

    except IOError:
        return ''


setup(
    name='{{cookiecutter.project_slug}}',
    version='{{cookiecutter.version}}',
    description='{{cookiecutter.short_description}}',
    long_description=_read("Readme.md"),
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url="{{ cookiecutter.github_url }}",
    setup_requires=['pytest-runner'],
    install_requires=[],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
    ],
)
