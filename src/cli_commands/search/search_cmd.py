"""
provides dir/files search cmd commands
"""

# third-party-lib
import click

# local-lib
import search_fun


@click.command()
@click.argument('path', nargs=1)
@click.option('-n', '--filename', help='search after specific filename')
@click.option('-t', '--filetype', help='search after specific filetype')
def search(path: str, filename: str = None, filetype: str = None):
    """
    cmd command for searching after files in a dir, default: search after all files in dir

    :param path: path to dir in which the search should begin
    :param filename: filename from target file
    :param filetype: filetype from target file/s
    """

    for filepath in search_fun.search(path, filename, filetype):
        click.echo(f"{filepath}")
    return


if __name__ == "__main__":
    search()
