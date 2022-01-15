# third-party-lib
import click

# local-lib
from . import search_fun


@click.command()
@click.argument('path', nargs=1)
@click.option('--filename', default=1, help='search after specific filename')
@click.option('--filetype', default=1, help='search after specific filetype')
def search(path: str, filename: str = None, filetype: str = None):
    search_fun.search(path, filename, filetype)


if __name__ == "__main__":
    search()
