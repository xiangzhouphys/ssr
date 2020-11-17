#!/usr/bin/env python

# Third party modules
import click

# First party modules
import ssr


@click.group()
@click.version_option(version=ssr.__version__)
def entry_point():
    """Awesomeproject spreads pure awesomeness."""
