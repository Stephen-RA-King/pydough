#!/usr/bin/env python
import os
import shutil
import subprocess
import sys
from pathlib import Path

SLUG_DIRECTORY = Path.cwd()
SRC_DIRECTORY = SLUG_DIRECTORY / "src"
PKG_DIRECTORY = SRC_DIRECTORY / "{{ cookiecutter.pkg_name }}"
TEST_DIRECTORY = SLUG_DIRECTORY / "tests"


def delete_director(items_to_delete):
    for item in items_to_delete:
        if item.is_dir():
            delete_directory(item)
        else:
            delete_file(item)


def delete_directory(directory):
    shutil.rmtree(directory, ignore_errors=True)


def delete_file(file):
    Path.unlink(file, missing_ok=True)


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


def pip_configure(command):
    execute(sys.executable, "-m", "pip", "config", "set", "global.disable-pip-version-check", command)


def update_basic_packages(packages):
    print("Checking basic packages for updates")
    for package in packages:
        if "#" in package:
            continue
        else:
            execute(sys.executable, "-m", "pip", "install", "--upgrade", "-q", package)


def init_git():
    print("Git: initialization and configuration")
    if not (SLUG_DIRECTORY / ".git").is_dir():
        execute("git", "config", "--global", "init.defaultBranch", "main", cwd=SLUG_DIRECTORY)
        execute("git", "init", cwd=SLUG_DIRECTORY)
        execute("git", "config", "commit.template", ".gitmessage", cwd=SLUG_DIRECTORY)


def install_pre_commit_hooks():
    print("pre-commit: Installing")
    execute(sys.executable, "-m", "pip", "install", "pre-commit")
    print("pre-commit: Installing git hook")
    execute("pre-commit", "install")
    print("pre-commit: Updating repos")
    execute("pre-commit", "autoupdate")


def generate_requirements():
    print("Generating requirements")
    execute(sys.executable, "-m", "pip", "install", "pip-tools")
    cwd = SLUG_DIRECTORY / "requirements"
    execute("pip-compile", "-q", "base.in", cwd=cwd)
    execute("pip-compile", "-q", "development.in", cwd=cwd)
    execute("pip-compile", "-q", "production.in", cwd=cwd)
    execute("pip-compile", "-q", "test.in", cwd=cwd)


def main():
    pip_configure("True")

    upgrade_basics_list = [
        "pip",
        "wheel",
        "setuptools",
    ]
    update_basic_packages(upgrade_basics_list)

    if "{{ cookiecutter.use_pytest }}".lower() != "y":
        delete_director([
            SLUG_DIRECTORY / "pytest.ini",
        ])

    if "{{ cookiecutter.command_line_interface }}".lower() != "click":
        delete_director([
            PKG_DIRECTORY / "cli.py",
            TEST_DIRECTORY / "test_cli.py"
        ])

    if "{{ cookiecutter.use_logging }}".lower() != "y":
        delete_director([
            SLUG_DIRECTORY / "logs",
        ])

    try:
        init_git()
    except Exception as e:
        print(e)

    if "{{ cookiecutter.use_pre_commit }}" == "y":
        try:
            install_pre_commit_hooks()
        except Exception as e:
            print(str(e))
            print("Failed to install pre-commit hooks. Please run `pre-commit install` manually")

    try:
        generate_requirements()
    except Exception as e:
        print(str(e))

    pip_configure("False")


if __name__ == "__main__":
    main()
