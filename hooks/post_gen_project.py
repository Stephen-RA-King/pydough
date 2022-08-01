#!/usr/bin/env python3
"""Utility tool to finalize installation after initial cookiecutter file copy."""

# Core Library modules
import logging
import os
import shutil
import subprocess
import sys
from pathlib import Path


SLUG_DIR = Path.cwd()
SRC_DIR = SLUG_DIR / "src"
LOG_DIR = SLUG_DIR / "logs"
PKG_DIR = SRC_DIR / "{{ cookiecutter.pkg_name }}"
TEST_DIR = SLUG_DIR / "tests"
REQ_DIR = SLUG_DIR / "requirements"


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(LOG_DIR / "post_gen.log")
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.DEBUG)
c_format = logging.Formatter("%(message)s")
f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)
logger.addHandler(c_handler)
logger.addHandler(f_handler)


def delete_director(items_to_delete):
    """Utility function to delete files or directories"""

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
        decoded_out = out.decode("utf-8")
        decoded_err = err.decode("utf-8")
        if err and not supress_exception:
            logger.exception(decoded_err)
            raise Exception(decoded_err)
    finally:
        logger.debug(f"Changing Directory to: {cur_dir}")
        os.chdir(cur_dir)


def file_word_replace(filepath: str, old_word: str, new_word: str) -> None:
    with open(filepath) as file:
        file_data = file.read()
    file_data = file_data.replace(old_word, new_word)
    with open(filepath, "w") as file:
        file.write(file_data)


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
        logger.info(f"...... package: {package}")
        if "#" in package:
            continue
        else:
            execute(sys.executable, "-m", "pip", "install", "--upgrade", "-q", package)


def init_git():
    if not (SLUG_DIR / ".git").is_dir():
        execute("git", "init", "--initial-branch={{ cookiecutter.initial_git_branch_name }}", cwd=SLUG_DIR)
        execute("git", "config", "commit.template", ".gitmessage", cwd=SLUG_DIR)
        execute("git", "config", "core.safecrlf", "false", cwd=SLUG_DIR)

        if "{{ cookiecutter.github_username }}":
            github_url = "".join(
                [
                    "/".join(
                        [
                            "https://github.com",
                            "{{ cookiecutter.github_username }}",
                            "{{ cookiecutter.project_name }}",
                        ]
                    ),
                    ".git",
                ]
            )
            logger.info(f"...... remote url: {github_url}")
            execute("git", "remote", "add", "origin", github_url, cwd=SLUG_DIR)


def install_pre_commit_hooks():
    execute("pre-commit", "install")
    execute("pre-commit", "autoupdate")
    if "{{ cookiecutter.use_commitizen }}".lower() == "y":
        execute("pre-commit", "install", "--hook-type", "commit-msg")


# exception suppressed due to "warnings.warn("Setuptools is replacing distutils.")"
def generate_requirements(requirements):
    for requirement in requirements:
        logger.info(f"...... {requirement[:-3]}.txt")
        execute("pip-compile", "-q", requirement, supress_exception=True, cwd=REQ_DIR)


def main():
    pip_configure("True")

    upgrade_basics_list = [
        "pip",
        "wheel",
        "setuptools",
        "build",
        "pip-tools",
        "pynacl",
        "keyring",
        "requests"
    ]

    if "{{ cookiecutter.version_control }}" == "python_semantic_release":
        upgrade_basics_list.append("python-semantic-release")

    logger.info("Upgrading and Installing Basic Packages")
    upgrade_package(upgrade_basics_list)

    config_files = [
        PKG_DIR / "config.ini",
        PKG_DIR / "config.json",
        PKG_DIR / "config.toml",
        PKG_DIR / "config.yaml",
    ]
    if "{{ cookiecutter.config_file }}" == "none":
        delete_director(config_files)
    elif "{{ cookiecutter.config_file }}" != "all":
        keep_file = "".join(["config.", "{{ cookiecutter.config_file }}"])
        config_files.remove(PKG_DIR / keep_file)
        delete_director(config_files)

    if "{{ cookiecutter.create_author_file }}".lower() != "y":
        delete_director(
            [
                SLUG_DIR / "AUTHORS.md",
            ]
        )

    if "{{ cookiecutter.include_example_scripts }}".lower() != "y":
        delete_director(
            [
                SLUG_DIR / "examples",
            ]
        )

    if "{{ cookiecutter.github_username }}" != "Stephen-RA-King":
        delete_director(
            [
                SLUG_DIR / "post_installation.py",
                SLUG_DIR / "_NOTES.docx",
                SLUG_DIR / "_TODO.txt"
            ]
        )
    else:
        os.rename("_NOTES.docx", "NOTES.docx")
        os.rename("_TODO.txt", "TODO.txt")

    if "{{ cookiecutter.use_docker }}".lower() != "y":
        delete_director(
            [
                SLUG_DIR / "Dockerfile",
            ]
        )

    if "{{ cookiecutter.version_control }}".lower() == "python_semantic_release":
        delete_director(
            [
                SLUG_DIR / ".bumpversion.cfg",
            ]
        )

    if "{{ cookiecutter.use_bandit }}".lower() != "y":
        delete_director(
            [
                SLUG_DIR / ".bandit.yml",
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
    else:
        delete_director(
            [
                SLUG_DIR / ".pre-commit-config.yaml",
            ]
        )

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

    os.rename(".gitignore_template", ".gitignore")

    pip_configure("False")


if __name__ == "__main__":
    main()
