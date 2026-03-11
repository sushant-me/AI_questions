"""
Package Python project for distribution.
"""

from setuptools import setup, find_packages

setup(
    name='example_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'numpy>=1.19.5',
    ],
    entry_points={
        'console_scripts': [
            'example_script=example_project.__main__:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A sample Python project for distribution',
    url='https://example.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)