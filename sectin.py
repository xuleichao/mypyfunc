'''

by xlc time:2017-09-12 17:10:48
'''
import sys
sys.path.append('D:/mypyfunc')

#把时间分段，seg_list是分段方式
def time_seg(seg_list,time): #时间分段函数
    if time < min(seg_list):
        return 0
    elif time >= max(seg_list):
        return len(seg_list) - 1
    else:
        i = 0
        while(i<(len(seg_list)-1)):
            if seg_list[i] <= time < seg_list[i + 1]:
                break
            else:
                i += 1
        return i + 1
