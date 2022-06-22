#!/usr/bin/env python3
# Core Library modules
from typing import Any

# Third party modules
{%- if cookiecutter.use_logging == 'y' %}
from {{ cookiecutter.pkg_name }} import logger
{% endif %}

{%- if cookiecutter.config_file == 'json' or cookiecutter.config_file == 'all' %}
from {{ cookiecutter.pkg_name }} import json_config{% endif %}
{%- if cookiecutter.config_file == 'ini' or cookiecutter.config_file == 'all' %}
from {{ cookiecutter.pkg_name }} import ini_config{% endif %}
{%- if cookiecutter.config_file == 'toml' or cookiecutter.config_file == 'all' %}
from {{ cookiecutter.pkg_name }} import toml_config{% endif %}
{%- if cookiecutter.config_file == 'yaml' or cookiecutter.config_file == 'all' %}
from {{ cookiecutter.pkg_name }} import yaml_config{% endif %}

def fizzbuzz(number_range: int) -> list:
    """Return integers 1 to N, but print “Fizz” if an integer is divisible by 3,
    “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer is
    divisible by both 3 and 5

    Parameters
    ----------
    number_range: int
        The maximum number that will be used

    Returns
    -------
    list
        The result will be returned as a list

    Examples
    --------
    >>> fizzbuzz(20)
    """
    result: list[Any] = []
    for num in range(1, number_range):
        if num % 15 == 0:
            result.append("FizzBuzz")
        elif num % 5 == 0:
            result.append("Buzz")
        elif num % 3 == 0:
            result.append("Fizz")
        else:
            result.append(num)
    {%- if cookiecutter.use_logging == 'y' %}
    logger.debug(f'fizzbuzz result: {result}'){% endif %}
    return result


def fibonacci(number_range: int) -> list:
    """series of numbers in which each number is the sum of the two that precede it

    Parameters
    ----------
    number_range: int
        The maximum number that will be used

    Returns
    -------
    list
        The result will be returned as a list

    Examples
    --------
    >>> fibonacci(20)
    """
    result: list = []
    a, b = 1, 1
    while True:
        if a >= number_range:
            {%- if cookiecutter.use_logging == 'y' %}
            logger.debug(f'fibonacci result: {result}'){% endif %}
            return result
        result.append(a)
        a, b = b, (a + b)
