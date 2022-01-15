"""
provides directory operation cmd commands
"""

# std-lib
import click

# local-lib
from src.cli_commands import dir_ops


@click.command(name='copy_files_to_dir')
@click.argument('type', nargs=1)
@click.argument('src_dir', nargs=1)
@click.argument('tar_dir', nargs=1)
@click.option('--drive', default=1, help='Hard-Drive')
def copy_files_in_dir(type: str, src_dir: str, tar_dir: str, drive: str):
    """
    copy specific files from src_dir in tar_dir

    :param type: file type
    :param src_dir: path to source directory which should be copied
    :param tar_dir: path to target directory in which the files get copied
    :param drive: system drive
    :return: None
    """
    click.echo(f"Copy {type} Files from {src_dir} to {tar_dir}")
    dir_ops.copy_files_in_dir(type, src_dir, tar_dir, drive)
    return


@click.command(name='lookup_content_dir')
@click.argument('dir_path', nargs=1)
def lookup_dir(dir_path: str):
    """
    prints content of given dir out

    :param dir_path: path to directory which content get printed out
    :return: None
    """
    click.echo(dir_ops.lookup_target_files(dir_path))
    return


@click.command(name='get-all-files')
@click.argument('path')
def get_all_files_from_dir(path: str):
    """
    prints out all elements in given dir

    :param path: path to target directory
    """
    click.echo(dir_ops.lookup_target_files(path))
    return


@click.command(name='copy')
@click.argument('src_dir')
@click.argument('tar_dir')
@click.option('-t', '--type', 'type_')
def copy_files(src_dir: str, tar_dir: str, type_=None):
    dir_ops.copy(src_dir, tar_dir, type_)
    return


# group all commands from module
@click.group()
def cli():
    """ creates command group """
    pass


cli.add_command(copy_files_in_dir)
cli.add_command(lookup_dir)
cli.add_command(copy_files)
cli.add_command(get_all_files_from_dir)
