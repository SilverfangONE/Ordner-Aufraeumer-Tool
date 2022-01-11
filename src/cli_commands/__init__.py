"""
provides cmd-commands for directory and arithmetic operations
"""

# std-lib
import click

# local-lib
from .calculator import cli as calc_cli
from .dir_sort import cli as dir_cli

# add cli groups to one cli group
cli = click.CommandCollection(sources=[calc_cli, dir_cli])


def lunch():
    """ starts CMD-Commands """
    cli()
