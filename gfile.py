import json

def get_file(path='c:/',file_type='.txt'):
    import os
    file = os.listdir(path)
    file = [i for i in file if file_type in i]
    return file

def json2lst(path): #把json文件反序列化
    f = open(path,'r',encoding='utf-8')
    f_str = f.readlines()
    f.close()

    f_lst = [json.loads(i) for i in f_str]
    return f_lst
