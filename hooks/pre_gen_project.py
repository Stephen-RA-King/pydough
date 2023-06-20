#!/usr/bin/env python3
"""Utility tool - executed before initial cookiecutter file copy."""

# Core Library modules
import os
import re
import subprocess
import sys


install_list = [
    "rich",
    "colorama",
    "tqdm"
]


def execute(*args, supress_exception=False, cwd=None):
    cur_dir = os.getcwd()
    try:
        if cwd:
            os.chdir(cwd)
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
        decoded_out = out.decode("utf-8")
        decoded_err = err.decode("utf-8")
        if err and not supress_exception:
            raise Exception(decoded_err)
    finally:
        os.chdir(cur_dir)


def upgrade_package(packages):
    print("Installing 3rd party packages")
    for package in packages:
        # print(f"...... package: {package}")
        if "#" in package:
            continue
        else:
            execute(sys.executable, "-m", "pip", "install", "--upgrade", "-q", package)


upgrade_package(install_list)

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
module_name = '{{ cookiecutter.project_slug}}'


if not re.match(MODULE_REGEX, module_name):
    """Utility function to check module name complies with PEP8"""

    print(
        'ERROR: The project slug (%s) is not a valid Python module name. '
        'Please do not use a - and use _ instead' % module_name)

    sys.exit(1)




