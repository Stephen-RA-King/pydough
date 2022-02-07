#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import click


@click.group()
def info():
    pass


@info.command(help="Display Author Name")
@click.option("-verbose", "--verbose", is_flag=True, help="set the verbosity")
def author(verbose):
    click.echo("Author name: {{ cookiecutter.author_name }}")
    if verbose:
        click.echo("Author eMail: {{ cookiecutter.email }}")


@info.command(help="Display Package Information")
@click.option("-verbose", "--verbose", is_flag=True, help="set the verbosity")
def pkg_info(verbose):
    click.echo("Package Version: {{ cookiecutter.version }}")
    if verbose:
        click.echo("{{ cookiecutter.pkg_name }}")
        click.echo("{{ cookiecutter.project_short_description }}")


@info.command(help="Displays the Python version")
def python():
    click.echo("{0.major}.{0.minor}.{0.micro}".format(sys.version_info))


if __name__ == '__main__':
    info()
