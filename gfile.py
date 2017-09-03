def get_file(path='c:/',file_type='.txt'):
    import os
    file = os.listdir(path)
    file = [i for i in file if file_type in i]
    return file
