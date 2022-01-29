#!/usr/bin/env python
import os
import shutil
import subprocess
import sys
from pathlib import Path

SLUG_DIRECTORY = Path.cwd()
SRC_DIRECTORY = SLUG_DIRECTORY / 'src'
PKG_DIRECTORY = SLUG_DIRECTORY / 'src' / '{{ cookiecutter.pkg_name }}'


def delete_director(items_to_delete):
    for item in items_to_delete:
        if item.is_dir():
            delete_directory(item)
        else:
            delete_file(item)


def delete_file(file):
    Path.unlink(file, missing_ok=True)


def delete_directory(directory):
    shutil.rmtree(directory, ignore_errors=True)


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


def update_basic_packages(packages):
    print("Checking basic packages for updates")
    for package in packages:
        execute(sys.executable, "-m", "pip", "install", "--upgrade", "-q", package)


def init_git():
    print("Git: initialization and configuration")
    if not (SLUG_DIRECTORY / '.git').is_dir():
        execute("git", "config", "--global", "init.defaultBranch", "main", cwd=SLUG_DIRECTORY)
        execute("git", "init", cwd=SLUG_DIRECTORY)
        execute("git", "config", "commit.template", ".gitmessage", cwd=SLUG_DIRECTORY)


def install_pre_commit_hooks():
    print("Installing pre-commit")
    execute(sys.executable, "-m", "pip", "install", "pre-commit")
    execute("pre-commit", "install")
    print("Updating pre-commit config to the latest repos' versions")
    execute("pre-commit", "autoupdate")


def generate_requirements():
    execute(sys.executable, "-m", "pip", "install", "pip-tools")
    cwd = SLUG_DIRECTORY / "requirements"
    execute("pip-compile", "-q", "base.in", cwd=cwd)
    execute("pip-compile", "-q", "development.in", cwd=cwd)
    execute("pip-compile", "-q", "production.in", cwd=cwd)
    execute("pip-compile", "-q", "test.in", cwd=cwd)


if __name__ == '__main__':
    upgrade_basics_list = [
        "pip",
        "wheel",
        "setuptools",
    ]
    update_basic_packages(upgrade_basics_list)

    if "{{ cookiecutter.use_pytest }}".lower() != "y":
        delete_director([
            SLUG_DIRECTORY / 'pytest.ini',
        ])

    if "{{ cookiecutter.use_flake8 }}".lower() != "y":
        delete_director([
            SLUG_DIRECTORY / '.flake8',
        ])

    if "{{ cookiecutter.use_log_files }}".lower() != "y":
        delete_director([
            SLUG_DIRECTORY / 'logs',
        ])

    try:
        init_git()
    except Exception as e:
        print(e)

    if '{{ cookiecutter.use_pre_commit }}' == 'y':
        try:
            install_pre_commit_hooks()
        except Exception as e:
            print(str(e))
            print("Failed to install pre-commit hooks. Please run `pre-commit install` manually")

    print("...Generating requirements")
    try:
        generate_requirements()
    except Exception as e:
        print(str(e))
