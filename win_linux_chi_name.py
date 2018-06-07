'''
1. 用于解决window 中文文件名转到Linux 后出现乱码。
原理为：由于两套系统的编码不同
首先将windows 下的文件名编码为英文、数字编码
然后在linux 系统下将编码解码为中文名
by xlc time:2018-05-10 17:21:48
'''
import sys
#sys.path.append('D:/svn_codes/source/public_fun')
import os
main_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
main_path = '/'.join(main_path.split('/')[:-1])
import hashlib
hl = hashlib.md5()

def bian_ma(folder, split_type='?'): #文件夹下所有文件
    folder = folder.replace('\\', '/')
    files = os.listdir(folder)
    bm_dct = {}
    for i in files:
        hl.update(i.encode(encoding='utf-8'))
        j = hl.hexdigest()
        bm_dct[i] = j
        os.rename(folder+'/'+i, folder+'/'+j)
    f = open(folder + '/bm_result.txt', 'w', encoding='utf-8')
    for i, j in bm_dct.items():
        abs_i = folder + '/' + i
        abs_j = folder + '/' + j
        f.write(abs_i + split_type + abs_j + '\n')
    f.close()

def batch_bm(filepath, split_type='?'):
    '''
    批量中文名编码
    返回键值对
    中文名与编码用空格隔开
    中文在左，编码在右边
    '''
    filepath = filepath.replace('\\', '/')
    path_split = filepath.split('/')[: -1]
    main_fd = '/'.join(path_split)
    f = open(filepath, 'r', encoding='utf-8').readlines()
    dct = {}
    file_pairs = [i.strip().split(split_type) for i in f]
    old_path = list(file_pairs.item())[0][0].split('/')[: -1]
    old_path = '/'.join(old_path)
    for i in file_pairs:
        dct[i[0].replace(old_path, main_fd)] = i[1].replace(old_path, main_fd)
    return dct

if __name__ == '__main__':
    filepath = r"C:\Users\e_gaoyunc\Desktop\新建文件夹\bm_result.txt"
    win_bm_dct = batch_bm(filepath)
    for i, j in win_bm_dct.items():
        os.rename(j, i)
        
    
