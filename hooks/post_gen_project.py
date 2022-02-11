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
f_handler = logging.FileHandler('logs/post_gen.log')
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.DEBUG)
c_format = logging.Formatter('%(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)
logger.addHandler(c_handler)
logger.addHandler(f_handler)


def delete_director(items_to_delete):
    for item in items_to_delete:
        if item.is_dir():
            logger.debug(f"Deleting Directory: {item}")
            shutil.rmtree(item, ignore_errors=True)
        else:
            logger.debug(f"Deleting File: {item}")
            Path.unlink(item, missing_ok=True)


def execute(*args, supress_exception=False, cwd=None):
    logger.debug(f"Executing command line: '{args}'")
    cur_dir = os.getcwd()
    logger.debug(f"Current Directory: {cur_dir}")
    try:
        if cwd:
            logger.debug(f"Changing Directory to: {cwd}")
            os.chdir(cwd)
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
        out = out.decode("utf-8")
        err = err.decode("utf-8")
        if err and not supress_exception:
            logger.exception(err)
            raise Exception(err)
        else:
            return out
    finally:
        logger.debug(f"Changing Directory to: {cur_dir}")
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
        logger.debug(f"Upgrading package: {package}")
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
        logger.debug(f"Analysing {requirement}")
        execute("pip-compile", "-q", requirement, cwd=REQ_DIR)


def main():
    pip_configure("True")

    upgrade_basics_list = [
        "pip",
        "wheel",
        "setuptools",
        "pip-tools",
    ]
    logger.info("Upgrading basic packages")
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
                PKG_DIR / "logging_config.yaml",
            ]
        )

    if "{{ cookiecutter.use_email_utility }}".lower() != "y":
        delete_director(
            [
                PKG_DIR / "email_config.ini",
                PKG_DIR / "send_email.py",
            ]
        )




    try:
        logger.info("git: Initializing & Configuring")
        init_git()
    except Exception as e:
        logger.exception(e)

    if "{{ cookiecutter.use_pre_commit }}" == "y":
        logger.info("pre-commit: configuring")
        try:
            upgrade_package(
                [
                    "pre-commit",
                ]
            )
            install_pre_commit_hooks()
        except Exception as e:
            logger.exception(e)

    try:
        req_list = [
            "base.in",
            "development.in",
            "production.in",
            "test.in",
        ]
        logger.info("Generating Requirements")
        generate_requirements(req_list)
    except Exception as e:
        logger.exception(e)

    pip_configure("False")


if __name__ == "__main__":
    main()
