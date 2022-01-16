"""
provides directory/files copy operation functions
"""

# std-lib
import shutil

# local-lib
from ..search.search_fun import search


# copy all files form dir and his subs in one target dir by default
def copy(src_path: str, tar_path, filename: str = None, filetype: str = None):
    for filepath in search(src_path, filename, filetype):
        shutil.copy(filepath, tar_path)
    return


# copy all files form source in structured dir
def copy_all_files_from_source_in_structured_dir():
    return
