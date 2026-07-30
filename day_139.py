"""
Create a Python package.
"""

from setuptools import setup, find_packages

setup(
    name='example_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
    ],
    entry_points={
        'console_scripts': [
            'example_command=example_package.module:main_function',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of the package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://example.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)