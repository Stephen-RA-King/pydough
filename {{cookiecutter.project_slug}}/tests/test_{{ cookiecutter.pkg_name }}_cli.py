#!/usr/bin/env python3
"""Tests for CLI scripts"""

# Core Library modules
import sys

# Third party modules
from click.testing import CliRunner

# First party modules
from {{ cookiecutter.pkg_name }} import {{ cookiecutter.pkg_name }}_cli


def test_author() -> None:
    """Test function to assert correct author name."""
    runner = CliRunner()
    result = runner.invoke({{ cookiecutter.pkg_name }}_cli.author)
    assert result.exit_code == 0
    assert result.output == "Author name: {{ cookiecutter.author_name }}\n"


def test_author_verbose() -> None:
    """Test function to assert correct verbose author name."""
    runner = CliRunner()
    result = runner.invoke({{ cookiecutter.pkg_name }}_cli.author, ["--verbose"])
    assert result.exit_code == 0
    assert (
        result.output == "Author name: {{ cookiecutter.author_name }}\n"
        "Author eMail: {{ cookiecutter.email }}\n"
    )


def test_author_help() -> None:
    """Test function to assert correct author help text."""
    runner = CliRunner()
    result = runner.invoke({{ cookiecutter.pkg_name }}_cli.author, ["--help"])
    assert result.exit_code == 0
    assert "  Display Author Name" in result.output

