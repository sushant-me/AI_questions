"""
Upload package to PyPI.
"""

import os
from setuptools import setup, find_packages
from setuptools.command.sdist import sdist

class PyPiSdist(sdist):
    def run(self):
        # Custom setup for PyPI package
        self.distribution.metadata.version = os.getenv('PACKAGE_VERSION', '0.1.0')
        sdist.run(self)

setup(
    name='example_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'numpy>=1.19.5',
    ],
    cmdclass={'sdist': PyPiSdist},
)