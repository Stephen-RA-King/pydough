#!/usr/bin/env python

# Third party modules
import click


@click.group()
@click.version_option(version="{{cookiecutter.version}}")
def entry_point():
    """Awesomeproject spreads pure awesomeness."""
