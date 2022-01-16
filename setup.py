"""
setuptools-module
"""

# extern-lib
from setuptools import setup
from setuptools import find_packages

setup(
    name='dir-cli',
    version='0.1.0',
    description='this package contains some cmd commands for directory operations',
    author='Luis-Boden',
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'dir = src.cli_commands:exe',
        ]
    }
)
