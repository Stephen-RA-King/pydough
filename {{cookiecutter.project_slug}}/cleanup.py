#!/usr/bin/env python

# Core Library modules
import os
import subprocess
import sys


def execute(*args, supress_exception=False, cwd=None):
    cur_dir = os.getcwd()
    try:
        if cwd:
            os.chdir(cwd)
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
        out = out.decode("utf-8")
        err = err.decode("utf-8")
        if err and not supress_exception:
            raise Exception(err)
        else:
            return out
    finally:
        os.chdir(cur_dir)


def remove_modules(module_list):
    current_list = execute(sys.executable, "-m", "pip", "freeze", "-q", "-l")
    print(current_list)
    for module in module_list:
        if module in current_list:
            execute(
                sys.executable,
                "-m",
                "pip",
                "uninstall",
                "-y",
                "-q",
                "--no-input",
                module,
            )


if __name__ == "__main__":
    remove_these_modules = [
        "arrow",
        "binaryornot",
        "certifi",
        "chardet",
        "charset-normalizer",
        "cookiecutter",
        "idna",
        "Jinja2",
        "jinja2-time",
        "MarkupSafe",
        "poyo",
        "python-dateutil",
        "python-slugify",
        "requests",
        "six",
        "text-unidecode",
        "urllib3",
    ]
    remove_modules(remove_these_modules)
