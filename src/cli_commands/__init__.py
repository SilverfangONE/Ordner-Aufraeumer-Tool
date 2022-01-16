"""
provides full cmd application for files searching, coping, shifting, deleting
"""

# third-party-lib
import click

# local-lib
from .search import search_cmd
from .copy import copy_cmd
from .delete import delete_cmd
from .shift import shift_cmd

cli = click.CommandCollection(
    sources=[
        search_cmd,
        copy_cmd,
        delete_cmd,
        shift_cmd]
)


def exe():
    cli()


if __name__ == '__main__':
    cli()
