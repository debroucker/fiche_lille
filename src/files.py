import os

def write_in_file(file_path, something_to_write):
    f = open(file_path, 'w', encoding='utf-8')
    f.write(something_to_write)
    f.close()

def read_file(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    data = f.readlines()
    f.close()
    return data

def read_all_file(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    data = f.read()
    f.close()
    return data

def create_dir(dir_path) :
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
