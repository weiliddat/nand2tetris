import os


def get_filepath_with_ext(filepath, ext):
    dirpath = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    filename_no_ext = os.path.splitext(filename)[0]
    outpath = os.path.join(dirpath, f"{filename_no_ext}.{ext}")
    return outpath
