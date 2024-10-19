import os


def rel_path(file_path: str, path: str):
    return os.path.abspath(os.path.join(os.path.dirname(file_path), path))
