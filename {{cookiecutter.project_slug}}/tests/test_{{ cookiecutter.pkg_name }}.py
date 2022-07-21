#!/usr/bin/env python3
"""Tests for package cookietest.py
To use tests either:
    1 - Use pip to install package as "editable"
            pip install -e .
    2 - Import pathmagic.py to enable tests to find the package
"""
{% if cookiecutter.use_pytest|lower == "y" -%}
# Third party modules

{%- else -%}
# Core Library modules
import unittest
{%- endif %}

# First party modules
from {{cookiecutter.pkg_name}} import {{cookiecutter.pkg_name}}


{% if cookiecutter.use_pytest|lower == "y" -%}
def test_get_config() -> None:
    num, result = {{cookiecutter.pkg_name}}.get_config()
    exp_result = [True for i in range(num)]
    print(result)
    assert result == exp_result

def test_fizzbuzz() -> None:
    result = {{ cookiecutter.pkg_name }}.fizzbuzz(16)
    print(result)
    assert result == [
        1,
        2,
        "Fizz",
        4,
        "Buzz",
        "Fizz",
        7,
        8,
        "Fizz",
        "Buzz",
        11,
        "Fizz",
        13,
        14,
        "FizzBuzz",
    ]

def test_fibonacci() -> None:
    result = {{ cookiecutter.pkg_name }}.fibonacci(10)
    print(result)
    assert result == [1, 1, 2, 3, 5, 8]

{%- else -%}
class {{cookiecutter.pkg_name}}TestCase(unittest.TestCase):
    def test_get_config(self) -> None:
        num, result = {{cookiecutter.pkg_name}}.get_config()
        exp_result = [True for i in range(num)]
        self.assertEqual(result == exp_result)

    def test_fizzbuzz(self) -> None:
        result = {{cookiecutter.pkg_name}}.fizzbuzz(10)
        self.assertEqual(result, [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz'])

    def test_fibonacci(self) -> None:
        result = {{cookiecutter.pkg_name}}.fibonacci(10)
        self.assertEqual(result, [1, 1, 2, 3, 5, 8])

{%- endif %}