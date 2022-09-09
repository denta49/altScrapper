import json
import os
import io


def get_files_path(directory, filenames=None):
    if filenames is None:
        filenames = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        filenames.append(f) if os.path.isfile(f) else get_files_path(f, filenames)
    return filenames


def split_file_into_words(file):
    file_words = []
    if file.endswith('.tsx') or file.endswith('.php') or file.endswith('.html') or file.endswith('.twig'):
        with io.open(file, 'r', encoding='windows-1252') as f:
            for line in f:
                file_words.append(line.split())
            f.close()
    else:
        pass
    return file_words


def check_if_alt(word):
    return word.startswith('alt=')


def get_file_alts(list_of_list_words):
    file_alts = []
    for li in list_of_list_words:
        if len(li) >= 1:
            if check_if_alt(li[0]):
                file_alts.append(li)
            else:
                pass
        else:
            pass
    return file_alts


def alt_filter(list):

    for word in list:
        return word.replace("alt=", '').replace("'", "").replace('"', '')


def get_alts(directory):
    file_paths = get_files_path(directory)
    dicti = {}

    for file in file_paths:
        file_words = split_file_into_words(file)
        if get_file_alts(file_words):
            arr = []
            for i in get_file_alts(file_words):
                print(i)
                arr.append(file)
                string=' '.join(map(str,i))
                dicti.update({string: f'{arr}'})
    print(dicti)
    return dicti


def save_json(dictionary, json_path, json_name):
    f = open(json_path + json_name, "w")
    json.dump(dictionary, f)
    f.close()


def main(directory, json_path, json_name):
    save_json(get_alts(directory), json_path, json_name)


directory = '/Users/p.wojenka/projekty/ogrodzenia-przemyslowe/src'
json_path = '/Users/p.wojenka/projekty/altScrapper/'
json_name = 'alts.json'

# add file extensions to read in split_file_into_words
# TODO: naprawic buga z encoding

main(directory, json_path, json_name)
