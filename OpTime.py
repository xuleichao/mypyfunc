'''
1. reg_time----函数是将一句话中的时间量正则表示出来。
2. str2_time----将一个表示时间量的字符串变为以天为单位的数字量，如: 半天--> 0.5 day, 一周 --> 7 days
by xlc time:2017-09-07 08:01:55
'''
import re

def reg_time(string):
    import re
    reg_str = r'([0-9]{1,3}|[一二三四五六七八九十半两])([+]?[ ]?[多]?[余]?[个]?[小]?)([周年月天时日]|分钟|分|星期)([余]?[左右]{0,2})'
    reg = re.compile(reg_str)
    time_str = re.findall(reg,string)
    return time_str

def str2time(string): #时间字符转化为时间量，单位统一为天
    time_str ={'年':365,'月':30,'周':7,'天':1,'小时':0.0416667,\
                '分钟':0.0006944}
    if '半' in string:
        time_num = 0.5
        unite = get_unite(string)
        days = time_num * unite
    else:
        time_num = reg_get_num(string)
        unite = get_unite(string)
        days = time_num * unite
    return days

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
    elif '天' in string:
        unite = time_str['天']
    elif '小时' in string:
        unite = time_str['小时']
    elif '分钟' in string:
        unite = time_str['分钟']
    else:
        print(string + '错误')
    return unite
