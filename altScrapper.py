import os

directory = '/Users/p.wojenka/projekty/service-b2c/service-b2c/src/sections'


def get_file_path(directory, filenames=None):
    if filenames is None:
        filenames = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        filenames.append(f) if os.path.isfile(f) else get_file_path(f, filenames)
    return filenames


def is_alt(elem):
    return elem == 'alt='


def split_file_into_letters(file):
    f = open(file, 'r')
    for word in f:
        print(word.split())
    f.close()

for i in get_file_path(directory):
    print(split_file_into_letters(i))



