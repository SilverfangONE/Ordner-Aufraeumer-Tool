"""
provides dir/files search cmd commands
"""

# third-party-lib
import click

# local-lib
from . import search_fun


@click.command()
@click.argument('path', nargs=1, help='path to dir in which the search should begin')
@click.option('--filename', default=1, help='search after specific filename')
@click.option('--filetype', default=1, help='search after specific filetype')
def search(path: str, filename: str = None, filetype: str = None):
    """
    cmd command for searching after files in a dir, default: search after all files in dir

    :param path: path to dir in which the search should begin
    :param filename: filename from target file
    :param filetype: filetype from target file/s
    """

    search_fun.search(path, filename, filetype)
    return


if __name__ == "__main__":
    search()
