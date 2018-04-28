'''

by xlc time:2018-04-20 14:51:40
'''
import sys
sys.path.append('D:/svn_codes/source/public_fun')
import os
main_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
main_path = '/'.join(main_path.split('/')[:-1])
import re

def regChiNum(string, withinQ=False):
    '''
    #返回值是一个list， 这个list 里的数字已经匹配到
    #不建议将list 中的内容join
    '''
    #大数正则
    reg_web = '([零一二三四五六七八九十百千万壹贰叁肆伍陆柒捌玖拾佰仟亿]+亿)?(零)?([一二三四五六七八九十百千壹贰叁肆伍陆柒捌玖拾佰仟]+万)?(零)?([一二三四五六七八九十百壹贰叁肆伍陆柒捌玖拾佰][千仟])?(零)?([一二三四五六七八九十壹贰叁肆伍陆柒捌玖拾][百佰])?(零)?([一二三四五六七八九壹贰叁肆伍陆柒捌玖]?[十拾])?(零)?([一二三四五六七八九壹贰叁肆伍陆柒捌玖])?(点)?([零一二三四五六七八九壹贰叁肆伍陆柒捌玖]?)?'
    #千以内的正则
    reg_qian = '([一二三四五六七八九十百壹贰叁肆伍陆柒捌玖拾佰][千仟])?(零)?([一二三四五六七八九十壹贰叁肆伍陆柒捌玖拾][百佰])?(零)?([一二三四五六七八九壹贰叁肆伍陆柒捌玖]?[十拾])?(零)?([一二三四五六七八九壹贰叁肆伍陆柒捌玖])?'
    if withinQ == False:
        result = re.findall(reg_web, string)
        result = [i for i in result if ''.join(i) !='']
        if result != []:
            return result[0]
        else:
            return []
    else:
        result = re.findall(reg_qian, string)
        result = [i for i in result if ''.join(i) !='']
        if result != []:
            return result[0]
        else:
            return []

def similar_zh(string):
    number_dict = {'捌': '八', '拾': '十', '佰': '百', '贰': '二', '柒': '七', '肆': '四', '陆': '六', '叁': '三', '仟': '千', '玖': '九', '壹': '一', '伍': '五'}#'零一二三四五六七八九十百千万壹贰叁肆伍陆柒捌玖拾'
    for i in string:
        value = number_dict.get(i)
        if value != None:
            string = string.replace(i, value)
    return string

def lst2num(lst):
    num = 0
    for i in range(len(lst)-1):
        if i % 2 == 0:
            num = num + (lst[i] * lst[i + 1])
    if len(lst) % 2 == 0:
        return num
    else:
        num += lst[-1]
        return num
        
def Chinum2Arab(reg_lst):
    '''
    # 将中文数字转换为阿拉伯数字
    '''
    if reg_lst == []:
        return ''
    danwei_dct = [['亿', 100000000], \
                  ['万', 10000],\
                  ['千', 1000], ['百', 100], ['十', 10], ['个', 1]]
    number_dct = {'一': 1, '九': 9, '四': 4, '八': 8, '六': 6, '二': 2, \
                  '五': 5, '零': 0, '七': 7, '三': 3, '十': 10, '百': 100, '千': 1000}
    danwei_keys = [i[0] for i in danwei_dct]
    result = []
    for i in reg_lst:
        for dw in danwei_keys:
            if dw in i:
                 i_new = i.replace(dw, '')
                 break
        else:
            i_new = i
            dw = '个'
        sub_rslt = []#捕捉单位的数值
        for n in i_new:
            sub_rslt.append(number_dct.get(n))
        result.append([sub_rslt, dw])
    real_result = []
    for i in result:
        i[0] = lst2num(i[0])
        for j in danwei_dct:
            if i[1] == j[0]:
                real_result.append(i[0] * j[1])
                break
    return sum(real_result)

def main(string):#传入经过同义词转换后的字符串
    '''
    传入经过同义词转换后的字符串
    '''
    test = string
    after_simi = similar_zh(test)
    reg_string = regChiNum(after_simi)
    rplc_s = ''.join(reg_string)
    t = Chinum2Arab(reg_string)
    t_str = str(t)
    test = test.replace(rplc_s, t_str)
    reg_string = regChiNum(test)
    if reg_string != []:
        test = main(test)
    return test    

if __name__ == '__main__':
    test = '一千一百亿零一千一百万零三' + '吼吼吼等等肆佰陆拾叁'
    test1 = 'ddddsasf'
    after_simi = similar_zh(test)
    a = main(after_simi)
