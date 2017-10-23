'''
1. reg_time----函数是将一句话中的时间量正则表示出来。
2. str2time----将一个表示时间量的字符串变为以天为单位的数字量，如: 半天--> 0.5 day, 一周 --> 7 days
3. 如果这里用着没问题就把这个目录里的str2time.py 这个文件删了吧
by xlc time:2017-09-07 08:01:55
'''
import re
import random

def reg_time(string):
    reg_str = r'([0-9]{1,3}|[一二三四五六七八九十半两])([+]?[ ]?[多]?[余]?[个]?[小]?)([周年月天时Hh日]|分钟|分|星期)([余]?(左右){0,1})' #(左右){0,1}
    reg = re.compile(reg_str)
    time_str = re.findall(reg,string)
    return time_str

def reg_date(string): #正则日期
    reg_ymd = r'\d{2,4}[年/.-](\d{1,2}[月/.-])?(\d{1,2}[日号]?)?'
    reg_ymd_time = r'\d{2,4}[年/. -]\d{1,2}[月/. -]\d{1,2}[日号 ]?[，,]?[ ]*\d{1,2}[点时：:]\d{1,2}[分]?'
    reg_md_time = r'\d{1,2}[月/. -]\d{1,2}[日号 ]?'
    reg_other = r'近?([0-9]{1,3}|[一二三四五六七八九十半两])个?半?余?([周年月天日]|小时|星期|分钟)[余半多]?[以之前后来底初]{1,2}来?'
    reg_other_plus = r'近([0-9]{1,3}|[一二三四五六七八九十半两])个?半?余?([周年月天日]|小时|星期|分钟)[余半多]?[以之前后来底初]{0,2}来?'
    ymd_0 = re.search(reg_ymd, string)
    ymd_1 = re.search(reg_other + '|' + reg_other_plus, string)
    md = re.search(reg_md_time, string) #月，日
    if ymd_1:
        return {'T':ymd_1.group()}
    elif ymd_0:
        return {'Y':ymd_0.group()}
    elif md:
        return {'M':md.group()}
    else:
        return {'N':''}
    
def str2time(string, with_rdm=True): #时间字符转化为时间量，单位统一为天
    time_str ={'年':365,'月':30,'周':7,'天':1,'小时':0.0416667,\
                '分钟':0.0006944}
    chi = ['半', '一', '二', '两', '三', '四', '五', '六', '七', '八', '九', '十']
    num = [0.5,1,2,2,3,4,5,6,7,8,9,10]
    chi2num = dict(zip(chi,num))
    unite = get_unite(string)
    if ('余' in string or '多' in string or '来' in string or \
       '约' in string or '+' in string) and with_rdm == True: # 用随机数的方法代替不确定时间的表示
        
        rdmtime = rdm_unite(unite)
        for i in chi:
            if i in string:
                time_num = chi2num[i]
                days = time_num * unite + rdmtime
                break
        else:
            time_num = reg_get_num(string)
            days = time_num * unite + rdmtime
    else:
        for i in chi:
            if i in string:
                try:
                    main_time = reg_get_num(string) #2年半的bug
                except:
                    main_time = 0
                time_num = main_time + chi2num[i]
                unite = get_unite(string)
                days = time_num * unite
                break
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
        rdm_time = random.randint(1,4)
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
    elif '周' in string or '礼拜' in string or '星期' in string:
        unite = time_str['周']
    elif '天' in string or '日' in string:
        unite = time_str['天']
    elif '小时' in string or '时' in string or 'H' in string or 'h' in string:
        unite = time_str['小时']
    elif '分钟' in string or '分' in string:
        unite = time_str['分钟']
    else:
        print(string + '错误')
    return unite
