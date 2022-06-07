
Math Parser 
===========

Math-Parser is a Python package to evaluate math expressions in strings using a LL-Compiler Algorithm with no 
dependencies, except the standard packages. 


Install
-------

Install the latest version directly from the source using Git:

    git clone
    cd Math-Parser
    python setup.py install

Usage
-----

To use this package, import the evaluate function and call it.

    from math_parser import evaluate

    expr = '2 * (10/2) + 5'
    evaluate(expr)

    >>> 15.0

In this version of the package it only accepts some operators:

- Addition (+);
- Subtraction (-);
- Multiplication (*);
- Division (/)
- Exponentiation (^)

Contact
-------

If you want to contact me, email me: victor.soeiro.araujo@gmail.com

Acknowledgements
----------------

This code was based on [Georg Nebehay](https://github.com/gnebehay) algorithm. Please check his code and documentation
for better understanding of this package, and give him a star.

