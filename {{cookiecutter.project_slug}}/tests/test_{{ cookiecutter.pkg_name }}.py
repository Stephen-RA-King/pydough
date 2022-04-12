#!/usr/bin/env python3
"""Tests for package cookietest.py
To use tests either:
    1 - Use pip to install package as "editable"
            pip install -e .
    2 - Import pathmagic.py to enable tests to find the package
"""
{% if cookiecutter.use_pytest|lower == "y" -%}
# Third party modules
import pytest
{%- else -%}
# Core Library modules
import unittest
{%- endif %}

# First party modules
from {{cookiecutter.pkg_name}} import {{cookiecutter.pkg_name}}


{% if cookiecutter.use_pytest|lower == "y" -%}
def test_fizzbuzz():
    result = {{ cookiecutter.pkg_name }}.fizzbuzz(10)
    assert result == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz']


def test_fibonacci():
    result = {{ cookiecutter.pkg_name }}.fibonacci(10)
    assert result == [1, 1, 2, 3, 5, 8]

{%- else -%}
class {{cookiecutter.pkg_name}}TestCase(unittest.TestCase):

    def test_fizzbuzz(self):
        result = {{cookiecutter.pkg_name}}.fizzbuzz(10)
        self.assertEqual(result, [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz'])

    def test_fibonacci(self):
        result = {{cookiecutter.pkg_name}}.fibonacci(10)
        self.assertEqual(result, [1, 1, 2, 3, 5, 8])

{%- endif %}