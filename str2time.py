'''

by xlc time:2017-09-07 08:01:55
'''
import sys
sys.path.append('D:/mypyfunc')
import re
import random

def str2time(string): #时间字符转化为时间量，单位统一为天
    time_str ={'年':365,'月':30,'周':7,'天':1,'小时':0.0416667,\
                '分钟':0.0006944}
    if '余' in string or '多' in string or '来' in string or \
       '约' in string: # 用随机数的方法代替不确定时间的表示
        unite = get_unite(string)
        rdmtime = rdm_unite(unite)   
        if '半' in string:
            time_num = 0.5
            #unite = get_unite(string)
            days = time_num * unite + rdmtime
        else:
            time_num = reg_get_num(string)
            #unite = get_unite(string)
            days = time_num * unite + rdmtime      
    else:
        if '半' in string:
            time_num = 0.5
            unite = get_unite(string)
            days = time_num * unite
        else:
            time_num = reg_get_num(string)
            unite = get_unite(string)
            days = time_num * unite
    return days

def rdm_unite(unite): #解决不确定时间的问题
    if unite == 365:
        rdm_time = random.randint(1,6)
        rdm_days = rdm_time * 30
    elif unite == 30:
        rdm_time = random.randint(1,15)
        rdm_days = rdm_time
    elif unite == 7:
        rdm_time = random.randint(1,3.5)
        rdm_days = rdm_time
    elif unite == 1:
        rdm_time = random.randint(1,12)
        rdm_days = rdm_time * 0.0416667
    elif unite == 0.0416667:
        rdm_time = random.randint(1,30)
        rdm_days = rdm_time * 0.0006944
    elif unite == 0.0006944:
        rdm_time = random.randint(1,30)
        rdm_days = rdm_time * 0.0000116
    return rdm_days
    
def reg_get_num(string): #正则提取文本中的数字
    reg = '\d{1,5}|[一二两俩三仨四五六七八九十]{1,2}'
    num = re.findall(reg,string)
    num = float(num[0])
    return num

def get_unite(string): #得到字符串的单位
    time_str ={'年':365,'月':30,'周':7,'天':1,'小时':0.0416667,\
                '分钟':0.0006944}
    if '年' in string:
        unite = time_str['年']
    elif '月' in string:
        unite = time_str['月']
    elif '周' in string:
        unite = time_str['周']
    elif '天' in string or '日' in string:
        unite = time_str['天']
    elif '小时' in string or '时' in string:
        unite = time_str['小时']
    elif '分钟' in string or '分' in string:
        unite = time_str['分钟']
    else:
        print(string + '错误')
    return unite
