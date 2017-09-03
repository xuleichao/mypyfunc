'''
查看文件中是否包含某个词语并返回文件名和词语出现的行数
'''

import sys
sys.path.append(r'D:\mypyfunc')
from gfile import get_file as gf

def find_word(path,file_type,word):
    files = gf(path,file_type)
    target_files = {}
    for name in files:
        f = open(path + '/' + name,'r',encoding='utf-8')
        f_str = f.readlines()
        f.close()

        #f_str = [i.strip() for i in f_str]
        #f_str = [i.split('\t') for i in f_str]

        for i in f_str:
            if word in i:
                target_files[name] = f_str.index(i) + 1
                print(name)
                print(f_str.index(i) + 1)
    return target_files

