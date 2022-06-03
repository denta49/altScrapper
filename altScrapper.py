import os


def get_file_path(directory, filenames=None):
    if filenames is None:
        filenames = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        filenames.append(f) if os.path.isfile(f) else get_file_path(f, filenames)
    return filenames


