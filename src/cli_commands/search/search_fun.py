"""
provides dir/files search operation functions
"""

# std lib
import os
import shutil

# third party-lib
import click


# search after one specific filename
def search_file_with_specific_name(path, filename=None):
    """
    search file with specific name

    :type path: str
    :type filename: str
    :return: full path searched file, if not found: None
    """

    for root, dirs, files in os.walk(path):
        for f in files:
            if os.path.basename(f) == filename:
                return os.path.abspath(f)
    return None


# search for all files in a dir
def search_files_in_dir(path: str):
    filepath_list = []

    def add_to_list(file):
        filepath_list.append(os.path.abspath(file))

    _iter_dir(path=path, filter_fun=add_to_list)
    return filepath_list


# search files in dir with a filter fun.
def search_files_with_specific_type():
    return


# iterate through the given source dir
def _iter_dir(path: str, filter_fun):
    """
    iterate through the given source dir

    :type path: str
    :param path: source directory
    :param filter_fun: filter function for further operations
    """

    for root, dirs, files in os.walk(path):
        for f in files:
            filter_fun(f)
    return

