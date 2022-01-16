"""
provides dir/files search operation functions
"""

# std lib
import os


def create_filter(filter_fun_list):
    def f(file):
        for fil in filter_fun_list:
            if not fil(file):
                return False
        return True

    return f


def search(path: str, filename: str = None, filetype: str = None):
    """
    search after files in a dir, default: search after all files in dir

    :param path: path to dir in which the search should begin
    :param filename: filename from target file
    :param filetype: filetype from target file/s
    """

    filter_fun_list = []

    # options
    if filename is not None:
        def f(filepath: str):
            # check if the filename is correct
            return True if os.path.splitext(filepath)[0] == filename or filepath == filename else False

        filter_fun_list.append(f)

    if filetype is not None:
        def f(filepath: str):
            # check if the filetype is correct
            return True if os.path.splitext(filepath)[1].replace('.', '') == filetype.replace('.', '') else False

        filter_fun_list.append(f)

    del f

    # filter execute default option
    def default_filter(file):
        return True

    return _iter_dir(
        path=path,
        # determine between default execution and advanced
        filter_fun=create_filter(filter_fun_list) if len(filter_fun_list) > 0 else default_filter
    )


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


# iterate through the given source dir
def _iter_dir(path: str, filter_fun):
    """
    iterate through the given source dir

    :type path: str
    :param path: source directory
    :param filter_fun: filter function for further operations
    """

    files_paths_list = []

    for root, dirs, files in os.walk(path):
        for f in files:
            # iter through filters
            if filter_fun(f):
                files_paths_list.append(os.path.abspath(f))
    return files_paths_list
