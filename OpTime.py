def reg_time(string):
    import re
    reg_str = r'([0-9]{1,3}|[一二三四五六七八九十半两])([+]?[ ]?[多]?[余]?[个]?[小]?)([周年月天时日]|分钟|分|星期)([余]?[左右]{0,2})'
    reg = re.compile(reg_str)
    time_str = re.findall(reg,string)
    return time_str
