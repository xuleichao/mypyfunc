'''

by xlc time:2017-09-06 18:23:37
'''
import sys
sys.path.append('D:/mypyfunc')
import json

def txt2lst(path,sign='\t'): #把text字段转化为lst
    f = open(path,'r',encoding='utf-8')
    f_str = f.readlines()
    f.close()

    f_str = [i.strip() for i in f_str]
    f_lst = [i.split(sign) for i in f_str]
    return f_lst

def lst2txt(lst,path,name,sign='\t',write_type='wb'): #把lst字符变为txt
    f = open(path + '/' + name,write_type)
    for i in lst:
        w_str = sign.join(i)
        f.write((w_str + '\n').encode('utf-8'))
    f.close()

def excel2lst(path,idx): #把excel数据变成list数据类型
    import xlrd
    
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(idx)
    nrows = sheet.nrows
    result = []
    for i in range(nrows):
        result.append(sheet.row_values(i))
    return result
    
