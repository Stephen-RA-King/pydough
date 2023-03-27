#!/usr/bin/env python3
"""Example script to demonstrate layout and testing."""
# Core Library modules
{%- if cookiecutter.use_logging == 'y' %}
import sys{% endif %}
{%- if cookiecutter.resource_file != 'none' %}
from importlib.resources import files, as_file{% endif %}
from typing import Any

# Third party modules
{%- if cookiecutter.resource_file == 'png' or cookiecutter.resource_file == 'all' %}
from PIL import Image{% endif %}

# Local modules
{%- if cookiecutter.config_file == 'ini' or cookiecutter.config_file == 'all' %}
from . import ini_config{% endif %}
{%- if cookiecutter.config_file == 'json' or cookiecutter.config_file == 'all' %}
from . import json_config{% endif %}
{%- if cookiecutter.use_logging == 'y' %}
from . import logger{% endif %}
{%- if cookiecutter.config_file == 'toml' or cookiecutter.config_file == 'all' %}
from . import toml_config{% endif %}
{%- if cookiecutter.config_file == 'yaml' or cookiecutter.config_file == 'all' %}
from . import yaml_config{% endif %}


{% if cookiecutter.config_file == 'json' or  cookiecutter.config_file == 'ini' or cookiecutter.config_file == 'toml' or cookiecutter.config_file == 'yaml' or cookiecutter.config_file == 'all' %}
def get_config() -> tuple:
    {% if cookiecutter.docstrings_style == 'numpy' %}
    """Return a configuration parameter from one of the configuration files.

    Returns
    -------
    tuple
        length of the tuple along with the debug setting from each config file.
    """{% else %}
    """Return a configuration parameter from one of the configuration files.

    Returns:
        tuple: length of the tuple along with the debug setting from each config file.
    """{% endif %}
    configs = [
        {%- if cookiecutter.config_file == 'ini' or cookiecutter.config_file == 'all' %}
        ini_config,{% endif %}
        {%- if cookiecutter.config_file == 'json' or cookiecutter.config_file == 'all' %}
        json_config,{% endif %}
        {%- if cookiecutter.config_file == 'toml' or cookiecutter.config_file == 'all' %}
        toml_config,{% endif %}
        {%- if cookiecutter.config_file == 'yaml' or cookiecutter.config_file == 'all' %}
        yaml_config{% endif %}
    ]
    config_result = []
    config_len = len(configs)

    for config in configs:
        config_result.append(bool(config["APP"]["DEBUG"]))
    return config_len, config_result
{% endif %}


{%- if cookiecutter.resource_file == 'pickle' or cookiecutter.resource_file == 'all' %}
def get_pickle():
    source = files("{{ cookiecutter.pkg_name }}.resources").joinpath('resource.pickle')
    with as_file(source) as _pickle_path:
        _pickle_text = _pickle_path.read_bytes()
        data = pickle.load(_pickle_text)
        return data
{% endif -%}


{% if cookiecutter.use_logging == 'y' %}
def handle_exception(exc_type, exc_value, exc_traceback):  # type: ignore
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception
{% endif %}

def fizzbuzz(number_range: int) -> list:
    {% if cookiecutter.docstrings_style == 'numpy' %}
    """Demonstrate one solution to the FizzBuzz problem.

    Return integers 1 to N, but print “Fizz” if an integer is divisible by 3,
    “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer is
    divisible by both 3 and 5

    Parameters
    ----------
    number_range : int
        The maximum number that will be used

    Returns
    -------
    list
        The result will be returned as a list

    Examples
    --------
    >>> fizzbuzz(20)
    """{% else %}
    """Demonstrate one solution to the FizzBuzz problem.

    Args:
        number_range (int): The maximum number that will be used

    Returns:
        list: The result will be returned as a list

    Examples:
        >>> fizzbuzz(20)
    """{% endif %}
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
    {% if cookiecutter.docstrings_style == 'numpy' %}
    """series of numbers in which each number is the sum of the two that precede it.

    Parameters
    ----------
    number_range : int
        The maximum number that will be used

    Returns
    -------
    list
        The result will be returned as a list

    Examples
    --------
    >>> fibonacci(20)
    """
    {% else %}
    """series of numbers in which each number is the sum of the two that precede it.

    Args:
        number_range (int): The maximum number that will be used

    Returns:
        list: The result will be returned as a list

    Examples:
        >>> fibonacci(20)
    """
    {% endif %}
    result: list = []
    a, b = 1, 1
    while True:
        if a >= number_range:
            {%- if cookiecutter.use_logging == 'y' %}
            logger.debug(f'fibonacci result: {result}'){% endif %}
            return result
        result.append(a)
        a, b = b, (a + b)


def main():
    print(fizzbuzz(20))
    print(fibonacci(20))


if __name__ == '__main__':
    raise SystemExit(main())




