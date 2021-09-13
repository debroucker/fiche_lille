def write_in_file(file_path, something_to_write):
    f = open(file_path, 'w', encoding='utf-8')
    f.write(something_to_write)
    f.close()


def read_file(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    data = f.readlines()
    f.close()
    return data
