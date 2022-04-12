#!/usr/bin/env python3
"""Example CLI module using click package."""

# Core Library modules
import sys

# Third party modules
import click


@click.group()
def info():
    """Creates container info to which other commands can be attached."""


@info.command(help="Display Author Name")
@click.option("-verbose", "--verbose", is_flag=True, help="set the verbosity")
def author(verbose):
    """Returns details about the Author."""
    click.echo("Author name: {{ cookiecutter.author_name }}")
    if verbose:
        click.echo("Author eMail: {{ cookiecutter.email }}")


@info.command(help="Display Package Information")
@click.option("-verbose", "--verbose", is_flag=True, help="set the verbosity")
def pkg_info(verbose):
    """Returns details about the package."""
    click.echo("Package Version: {{ cookiecutter.version }}")
    if verbose:
        click.echo("{{ cookiecutter.pkg_name }}")
        click.echo("{{ cookiecutter.project_short_description }}")


@info.command(help="Displays the Python version")
def python():
    """Returns details about the Python version."""
    click.echo("{0.major}.{0.minor}.{0.micro}".format(sys.version_info))


if __name__ == "__main__":
    """Creates entry point for the CLI"""
    info()
