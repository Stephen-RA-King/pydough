#!/usr/bin/env python3
"""Example CLI module using click package."""


# Third party modules
import click


@click.group()
def info() -> None:
    """Creates container info to which other commands can be attached."""


@info.command(help="Display Author Name")
@click.option("-verbose", "--verbose", is_flag=True, help="set the verbosity")
def author(verbose: str) -> None:
    """Returns details about the Author."""
    click.echo("Author name: {{ cookiecutter.author_name }}")
    if verbose:
        click.echo("Author eMail: {{ cookiecutter.email }}")


if __name__ == "__main__":
    info()
