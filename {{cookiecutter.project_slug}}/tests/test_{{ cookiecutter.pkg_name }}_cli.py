#!/usr/bin/env python3
"""Tests for CLI scripts"""

# Core Library modules
import sys

# Third party modules
from click.testing import CliRunner

# First party modules
from {{ cookiecutter.pkg_name }} import {{ cookiecutter.pkg_name }}_cli


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

