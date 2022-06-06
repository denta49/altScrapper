import os

directory = '/Users/p.wojenka/projekty/service-b2c/service-b2c/src/components'


def get_files_path(directory, filenames=None):
    if filenames is None:
        filenames = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        filenames.append(f) if os.path.isfile(f) else get_files_path(f, filenames)
    return filenames


def split_file_into_words(file):
    f = open(file, 'r')
    file_words = []
    for line in f:
        file_words.append(line.split())
    f.close()
    return file_words


def check_if_alt(word):
    return word.startswith('alt=')


def get_file_alts(list_of_list_words):
    file_alts = []
    for li in list_of_list_words:
        for word in li:
            if check_if_alt(word):
                file_alts.append(word)
            else:
                pass
    return file_alts


def alt_filter(word):
    return word.replace("alt=", '')


def get_alts(directory):
    file_paths = get_files_path(directory)
    alts = []

    for file in file_paths:
        file_words = split_file_into_words(file)
        temporary = file
        if get_file_alts(file_words):
            print(file)
            #TODO: czemu to printuje pojedyncz litery jak dam append?
            alts.append(get_file_alts(file_words))
    return alts


def alts_filter(directory):
    list_of_alts = get_alts(directory)
    clear_alts = []
    for ls in list_of_alts:
        for alt in ls:
            clear_alts.append(alt_filter(alt))
    print(clear_alts)
    return clear_alts


alts_filter(directory)






