#!/usr/bin/env python3
"""Utility tool - executed before initial cookiecutter file copy."""

# Core Library modules
import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
module_name = '{{ cookiecutter.project_slug}}'


if not re.match(MODULE_REGEX, module_name):
    """Utility function to check module name complies with PEP8"""

    print(
        'ERROR: The project slug (%s) is not a valid Python module name. '
        'Please do not use a - and use _ instead' % module_name)

    sys.exit(1)
