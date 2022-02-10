#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
import sys
from pathlib import Path
import logging


SLUG_DIR = Path.cwd()
SRC_DIR = SLUG_DIR / "src"
PKG_DIR = SRC_DIR / "{{ cookiecutter.pkg_name }}"
TEST_DIR = SLUG_DIR / "tests"
REQ_DIR = SLUG_DIR / "requirements"


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('post_gen.log')
c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)
logger.addHandler(c_handler)
logger.addHandler(f_handler)


def delete_director(items_to_delete):
    for item in items_to_delete:
        if item.is_dir():
            logger.info(f"Deleting Directory: {item}")
            shutil.rmtree(item, ignore_errors=True)
        else:
            logger.info(f"Deleting File: {item}")
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
    execute(
        sys.executable,
        "-m",
        "pip",
        "config",
        "set",
        "global.disable-pip-version-check",
        command,
    )


def upgrade_package(packages):
    for package in packages:
        if "#" in package:
            continue
        else:
            execute(sys.executable, "-m", "pip", "install", "--upgrade", "-q", package)


def init_git():
    if not (SLUG_DIR / ".git").is_dir():
        execute("git", "config", "--global", "init.defaultBranch", "main", cwd=SLUG_DIR)
        execute("git", "init", cwd=SLUG_DIR)
        execute("git", "config", "commit.template", ".gitmessage", cwd=SLUG_DIR)


def install_pre_commit_hooks():
    execute("pre-commit", "install")
    execute("pre-commit", "autoupdate")


def generate_requirements(requirements):
    for requirement in requirements:
        execute("pip-compile", "-q", requirement, cwd=REQ_DIR)


def main():
    logger = config_logging()
    logger.info("logger configured")

    pip_configure("True")

    upgrade_basics_list = [
        "pip",
        "wheel",
        "setuptools",
        "pip-tools",
    ]
    upgrade_package(upgrade_basics_list)

    if "{{ cookiecutter.create_author_file }}".lower() != "y":
        delete_director(
            [
                SLUG_DIR / "AUTHORS.md",
            ]
        )

    if "{{ cookiecutter.command_line_interface }}".lower() != "click":
        delete_director([PKG_DIR / "cli.py", TEST_DIR / "test_cli.py"])

    if "{{ cookiecutter.use_logging }}".lower() != "y":
        delete_director(
            [
                SLUG_DIR / "logs",
            ]
        )

    try:
        init_git()
    except Exception as e:
        print(e)
        print("Failed to Initialize Git")

    if "{{ cookiecutter.use_pre_commit }}" == "y":
        try:
            upgrade_package(
                [
                    "pre-commit",
                ]
            )
            install_pre_commit_hooks()
        except Exception as e:
            print(e)
            print(
                "Failed to install pre-commit hooks. Please run `pre-commit install` manually"
            )

    try:
        req_list = [
            "base.in",
            "development.in",
            "production.in",
            "test.in",
        ]
        generate_requirements(req_list)
    except Exception as e:
        print(e)
        print("Failed to Generate Requirements")

    pip_configure("False")


if __name__ == "__main__":
    main()
