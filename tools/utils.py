import os
from typing import Iterable

from genericpath import isdir, isfile


def get_vm_filepaths(path: str) -> list[str]:
    dirpath = os.path.dirname(path)
    filenames = os.listdir(dirpath)
    return [
        os.path.join(dirpath, filename)
        for filename in filenames
        if os.path.splitext(filename)[1] == ".vm"
    ]


def get_asm_filepath_from_path(path: str) -> str:
    if isfile(path):
        dirpath = os.path.dirname(path)
        filename = os.path.splitext(os.path.basename(path))[0] + ".asm"
        return os.path.normpath(os.path.join(dirpath, filename))
    elif isdir(path):
        filename = (
            os.path.split(path)[1]
            if os.path.split(path)[1]
            else os.path.split(os.path.split(path)[0])[1]
        ) + ".asm"
        return os.path.normpath(os.path.join(path, filename))
    else:
        raise ValueError(f"Invalid path {path}")


def get_filepath_with_ext(filepath: str, ext: str) -> str:
    dirpath = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    filename_no_ext = os.path.splitext(filename)[0]
    outpath = os.path.join(dirpath, f"{filename_no_ext}.{ext}")
    return outpath


def get_filename_no_ext(filepath: str) -> str:
    filename = os.path.basename(filepath)
    filename_no_ext = os.path.splitext(filename)[0]
    return filename_no_ext


def flatten(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x
