
from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent
README = (HERE / 'README.md').read_text()
REQUIRES = (HERE / 'requirements.txt').read_text().splitlines()

NAME = 'Math-Parser'
VERSION = '0.1'
DESCRIPTION = 'This package evaluates mathematics expressions written in string safely.'
AUTHOR = 'Victor Soeiro'
AUTHOR_EMAIL = 'victor.soeiro.araujo@gmail.com'
URL = 'https://github.com/victor-soeiro/Math-Parser'
LICENSE = 'MIT'
PYTHON_VER = '>=3.6'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(),
    install_requires=REQUIRES,
    python_requires=PYTHON_VER,
    keywords=[
        'mathematics', 'expressions', 'compilers', 'evaluation'
    ]
)
