# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name='fuzzy_self_driving',
    version='1.0',
    author='minhdao',
    description='Python Chess Project',
    packages=find_packages(exclude=[
        'docs',
        'tests',
        'static',
        'templates',
        '.gitignore',
        'README.md',
        'images',
        '.vscode',
    ]),
    install_requires=[
        'pylint',
        'autopep8',
        'rope',
        'pygame',
        'scipy',
        'xlrd==1.2.0'
    ]
)
