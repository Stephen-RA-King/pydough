#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
import sys
from pathlib import Path

SLUG_DIR = Path.cwd()
SRC_DIR = SLUG_DIR / "src"
PKG_DIR = SRC_DIR / "{{ cookiecutter.pkg_name }}"
TEST_DIR = SLUG_DIR / "tests"
REQ_DIR = SLUG_DIR / "requirements"


def delete_director(items_to_delete):
    for item in items_to_delete:
        if item.is_dir():
            shutil.rmtree(item, ignore_errors=True)
        else:
            Path.unlink(item, missing_ok=True)


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


def upgrade_package(packages):
    for package in packages:
        print(f"Installing / Upgrading package: {package}")
        if "#" in package:
            continue
        else:
            execute(sys.executable, "-m", "pip", "install", "--upgrade", "-q", package)


def init_git():
    print("Git: initialization and configuration")
    if not (SLUG_DIR / ".git").is_dir():
        execute("git", "config", "--global", "init.defaultBranch", "main", cwd=SLUG_DIR)
        execute("git", "init", cwd=SLUG_DIR)
        execute("git", "config", "commit.template", ".gitmessage", cwd=SLUG_DIR)


def install_pre_commit_hooks():
    # print("pre-commit: Installing")
    # execute(sys.executable, "-m", "pip", "install", "pre-commit")
    print("pre-commit: Installing git hook")
    execute("pre-commit", "install")
    print("pre-commit: Updating repos")
    execute("pre-commit", "autoupdate")


def generate_requirements(requirements):
    print("Generating requirements")
    for requirement in requirements:
        print(f"Processing requirement: {requirement}")
        execute("pip-compile", "-q", requirement, cwd=REQ_DIR)


def main():
    pip_configure("True")

    upgrade_basics_list = [
        "pip",
        "wheel",
        "setuptools",
        "pip-tools"
    ]
    upgrade_package(upgrade_basics_list)

    if "{{ cookiecutter.create_author_file }}".lower() != "y":
        delete_director([
            SLUG_DIR / "AUTHORS.md",
        ])

    if "{{ cookiecutter.command_line_interface }}".lower() != "click":
        delete_director([
            PKG_DIR / "cli.py",
            TEST_DIR / "test_cli.py"
        ])

    if "{{ cookiecutter.use_logging }}".lower() != "y":
        delete_director([
            SLUG_DIR / "logs",
        ])

    try:
        init_git()
    except Exception as e:
        print(e)

    if "{{ cookiecutter.use_pre_commit }}" == "y":
        try:
            upgrade_package(["pre-commit", ])
            install_pre_commit_hooks()
        except Exception as e:
            print(str(e))
            print("Failed to install pre-commit hooks. Please run `pre-commit install` manually")

    try:
        req_list = [
            "base.in",
            "development.in",
            "production.in",
            "test.in",
        ]
        generate_requirements(req_list)
    except Exception as e:
        print(str(e))

    pip_configure("False")


if __name__ == "__main__":
    main()
