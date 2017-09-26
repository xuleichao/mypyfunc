import json
import numpy as np


def cos_smlrt(a, b, use_dct=1): # 计算两个向量的余弦相似度，a,b为两个数字列表
    if type(a) == type('xlc'):
        import jieba
        if use_dct == 1:
            jieba.load_userdict(r'C:\Users\e_gaoyunc\Desktop\userdct.txt')
        a_lst = jieba.lcut(a)
        b_lst = jieba.lcut(b)
        a_b_set = set(a_lst) | set(b_lst) #集合
        a_matrix = [] # a 的词语序列
        b_matrix = []
        for i in a_b_set:
            a_matrix.append(a_lst.count(i))
            b_matrix.append(b_lst.count(i))
        a = a_matrix
        b = b_matrix
        print(a, a_lst, b, b_lst)
    a = np.array(a)
    b = np.array(b)
    mod_a = np.sqrt(sum(a * a))
    mod_b = np.sqrt(sum(b * b))
    fz_up = sum(a * b) # 分子
    cos = fz_up / (mod_a * mod_b)
    return cos

if __name__ != '__main__':
    cos_smlrt('a', 'b')




'''
f=open('C:/Users/e_gaoyunc/Desktop/zsfc.txt','r')
fc = f.readlines()
f.close()

fc_lst_cx = [json.loads(i) for i in fc[:100]]
length = len(fc_lst_cx)
fc_lst = []
for i in fc_lst_cx:
    fc_s_lst = [j[0] for j in i]
    fc_lst.append(fc_s_lst)

cosM = np.zeros((length,length)) #  构建cos值的矩阵
for i in range(length):
    for j in range(length):
        all_cy = list(set(fc_lst[i]) | set(fc_lst[j]))
        count_i = [fc_lst[i].count(cy) for cy in all_cy]
        count_j = [fc_lst[j].count(cy) for cy in all_cy]
        cosM[i][j] = cos_smlrt(count_i,count_j)
'''
