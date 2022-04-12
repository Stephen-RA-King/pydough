#!/usr/bin/env python3
"""Tests for CLI scripts"""

# Core Library modules
import sys

# Third party modules
from click.testing import CliRunner

# First party modules
from src.{{ cookiecutter.pkg_name }} import cli


def test_author():
    """Test function to assert correct author name."""
    runner = CliRunner()
    result = runner.invoke(cli.author)
    assert result.exit_code == 0
    assert result.output == "Author name: {{ cookiecutter.author_name }}\n"


def test_author_verbose():
    """Test function to assert correct verbose author name."""
    runner = CliRunner()
    result = runner.invoke(cli.author, ["--verbose"])
    assert result.exit_code == 0
    assert (
        result.output == "Author name: {{ cookiecutter.author_name }}\n"
        "Author eMail: {{ cookiecutter.email }}\n"
    )


def test_author_help():
    """Test function to assert correct author help text."""
    runner = CliRunner()
    result = runner.invoke(cli.author, ["--help"])
    assert result.exit_code == 0
    assert "  Display Author Name" in result.output


def test_pkg_info():
    """Test function to assert correct package information."""
    runner = CliRunner()
    result = runner.invoke(cli.pkg_info)
    assert result.exit_code == 0
    assert result.output == "Package Version: {{ cookiecutter.version }}\n"


def test_pkg_info_verbose():
    """Test function to assert correct verbose package information."""
    runner = CliRunner()
    result = runner.invoke(cli.pkg_info, ["--verbose"])
    assert result.exit_code == 0
    assert (
        result.output == "Package Version: {{ cookiecutter.version }}\n"
        "{{ cookiecutter.pkg_name }}\n"
        "{{ cookiecutter.project_short_description }}\n"
    )


def test_python_version():
    """Test function to assert python version."""
    version = "{0.major}.{0.minor}.{0.micro}".format(sys.version_info)
    runner = CliRunner()
    result = runner.invoke(cli.python)
    assert result.exit_code == 0
    assert result.output == f"{version}\n"


def test_pkg_info_help():
    """Test function to assert correct package information help text."""
    runner = CliRunner()
    result = runner.invoke(cli.pkg_info, ["--help"])
    assert result.exit_code == 0
    assert "  Display Package Information" in result.output
