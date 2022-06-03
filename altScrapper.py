import os

directory = '/Users/p.wojenka/projekty/service-b2c/service-b2c/src/components'


def get_files_path(directory, filenames=None):
    if filenames is None:
        filenames = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        filenames.append(f) if os.path.isfile(f) else get_files_path(f, filenames)
    return filenames


def is_alt(elem):
    return elem == 'alt='


def split_file_into_words(file):
    f = open(file, 'r')
    file_words = []
    for line in f:
        file_words.append(line.split())
    print(file_words)
    f.close()





