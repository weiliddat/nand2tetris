import os


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
