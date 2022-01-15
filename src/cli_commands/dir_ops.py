"""
provides directory operations functions
"""

# std lib
import os
import shutil

# third party-lib
import click


def get_all_files_for_type(type_: str):
    """


    :param type_:
    :return: get all files from specific type from hard drive
    """

    return


def copy_files_in_dir(type_: str, src_dir: str, tar_dir: str, drive="C"):
    """
    copy all files from specific type in given dir or in new on in current dir
    """

    return

# walk trough directory and call given callback function with file path
def lookup_target_files(path: str, filter_fun, op_fun, tar_path, type_=None):

    for root, dirs, files in os.walk(path):
        # walk trough the dir-tree and search files with the filter_fun

        for f in files:
            # filters with custom filter_fun

            if filter_fun(f_type=type, tar_file=f):
                click.echo(f"{f} from {path}")

                # custom operation for every match
                op_fun(file=os.path.join(f, path), tar_path)


def copy(src_path: str, target_path: str, type_: str):

    # print out searched type
    click.echo(f"type: {type_}\n")

    # create filter fun for searching files
    filter_ = create_filter(type_)

    def op(file, root, tar_path):
        shutil.copy(os.path.join(root, file), tar_path)

    lookup_target_files(src_path, create_filter(type_), op)


def clear(path: str, type_: str):
    click.echo('Act: Clear')

    if type_ is None:
        # no iter clean hole dir
        pass
    else:
        # iter with filter trough dir tree
        pass
    return




def create_filter(type_):
    # typ arg not set
    if type_ is None:
        def f(f_type, tar_file): return True

        return f

    # passes only files with given typ
    def f(f_type, tar_file):
        if tar_file.split(".")[-1] == f_type:
            return True

    return f
