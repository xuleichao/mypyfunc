'''

by xlc time:2018-12-20 08:35:40
'''
import sys
#sys.path.append('D:/svn_codes/source/public_fun')
import os
main_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
main_path = '/'.join(main_path.split('/')[:-1])
from load_dd import load_dd
import numpy as np
from numpy import *

def P_of_mu_sigama(x, mu, sigama):
    # P(x|mu, sigama)
    #print(x)
    #print(mu)
    #print(sigama)
    x = mat(np.array(x))
    mu = mat(np.array(mu))
    sigama = mat(np.array(sigama))
    
    n = sigama.shape[0] # 矩阵的大小
    # 行列式的值
    sigama_det = np.linalg.det(sigama)
    # 矩阵的逆
    sigama_reverse = sigama.I
    P_forth = 1/((2*np.pi) ** (1/n)) * sigama_det ** 0.5
    P_back = -0.5 * (x - mu) * sigama_reverse * (x - mu).T
    P = P_forth * exp(P_back)
    #print(x, mu, P, 123456)
    return P

def gamma_i_j_cal(x, mu_lst, sigama_lst, weight_lst, k):
    # 全概率计算
    P_sum = 0
    sub_prob = []
    for i in range(len(weight_lst)):
        P = P_of_mu_sigama(x, mu_lst[i], sigama_lst[i])
        sub_P = weight_lst[i] * P
        P_sum += sub_P
        sub_prob.append(sub_P)

    # gamma_ij 计算
    result = {}
    for _ in range(len(sub_prob)):
        i = k
        result[str(i)+'_x'] = (sub_prob[i] / P_sum).tolist()[0][0]
        break
    #print(result, 1234565)
    return result
        
def new_mu_vector_cal(datasets, mu_lst, sigama_lst, k, weight_lst):
    '''
    - k: 第几个高斯分量
    '''
    result = {}
    for _ in range(len(weight_lst)):
        i = k
        result[str(i) + '_sum_gamma_ij'] = 0
        result[str(i) + '_sum_gamma_ij_x'] = np.zeros(len(datasets[0]))
        break
    mu = mu_lst[k]
    sigama = sigama_lst[k]
    for i in datasets:
        for _ in range(len(weight_lst)):
            gamma_i = gamma_i_j_cal(i, mu_lst, sigama_lst, weight_lst, k)
            gamma_i_k = gamma_i[str(k)+'_x']
            gamma_ij_x = gamma_i_k * np.array(i)
            result[str(k) + '_sum_gamma_ij'] += gamma_i_k
            result[str(k) + '_sum_gamma_ij_x'] += gamma_ij_x
            break
    new_result = {}
    for _ in range(len(weight_lst)):
        i = k
        new_result[str(i)+'_mu'] = result[str(i) + '_sum_gamma_ij_x'] / result[str(i) + '_sum_gamma_ij']
        break
    return new_result

def new_sigama_cal(datasets, mu, sigama, k, weight_lst):
    '''
    - k: 第几个高斯分量
    '''
    result = {}
    for _ in range(len(weight_lst)):
        i = k
        result[str(i) + '_sum_sigama_ij'] = 0
        result[str(i) + '_sum_sigama_ij_x'] = np.zeros((len(datasets[0]), len(datasets[0])))
        break
    for i in datasets:
        gamma_i = gamma_i_j_cal(i, mu, sigama, weight_lst, k)
        for _ in range(len(weight_lst)):
            
            gamma_i_k = gamma_i[str(k)+'_x']
            gamma_ij_x = gamma_i_k * mat(np.array(i)).T * mat(np.array(i))
        
            result[str(k) + '_sum_sigama_ij'] += gamma_i_k
            result[str(k) + '_sum_sigama_ij_x'] += gamma_ij_x
            break
    new_result = {}
    for _ in range(len(weight_lst)):
        i = k
        new_result[str(i)+'_sigama'] = result[str(i) + '_sum_sigama_ij_x'] / result[str(i) + '_sum_sigama_ij']
        break
    return new_result

def new_weight_cal(datasets, mu, sigama, k, weight_lst):
    '''
    - k: 第几个高斯分量
    '''
    result = {}
    for _ in range(len(weight_lst)):
        i = k
        result[str(i) + '_weight_i'] = 0
        break
    for i in datasets:
        gamma_i = gamma_i_j_cal(i, mu, sigama, weight_lst, k)
        for _ in range(len(weight_lst)):
            gamma_i_k = gamma_i[str(k)+'_x']
            result[str(k) + '_weight_i'] += gamma_i_k
            break
    new_result = {}
    for _ in range(len(weight_lst)):
        i = k
        new_result[str(i)+'_weight_i'] = result[str(i) + '_weight_i'] / len(datasets)
        break
    return new_result

def E_step(datasets):
    '''
    - E步
    - 根据初始化的模型参数更新每一条数据属于第i个高斯模型的概率
    '''
    pass

def M_step(datasets):
    '''
    - M步
    - 根据新的后验概率更新模型参数
    '''
    pass

def E_M(datasets, mu_lst, gamma_lst, weight_lst):
    pass
    

if __name__ == '__main__':
    # E_M 过程
    datasets = load_dd()
    # 参数初始化
    # 平均值
    mu_lst = [np.array(datasets[5]), np.array(datasets[21]), np.array(datasets[26])]
    # 协方差
    sigama_lst = [np.array([[0.1, 0],
                           [0, 0.1]], dtype='float64'),
                 np.array([[.1, 0],
                           [0, .1]], dtype='float64'),
                  np.array([[.1, 0],
                           [0, .1]], dtype='float64')]
    # 高斯的权重
    weight_lst = [0.3333, 0.3333, 0.33333]
    num = 10 # 迭代次数
    for i in range(num):
        #print(mu_lst)
        #print(sigama_lst)
        #print(weight_lst)
        new_mu_lst = []
        new_sigama_lst = []
        new_weight_lst = []
        
        for j in range(len(mu_lst)):
            mu = mu_lst[j]
            sigama = sigama_lst[j]
            weight = weight_lst[j]
            new_mu = new_mu_vector_cal(datasets, mu_lst, sigama_lst, j, weight_lst)
            new_sigama = new_sigama_cal(datasets, mu_lst, sigama_lst, j, weight_lst)
            new_weight = new_weight_cal(datasets, mu_lst, sigama_lst, j, weight_lst)
            new_mu_lst.append(list(new_mu.values())[0])
            new_sigama_lst.append(list(new_sigama.values())[0])
            new_weight_lst.append(list(new_weight.values())[0])
        mu_lst = new_mu_lst
        sigama_lst = new_sigama_lst
        weight_lst = new_weight_lst
        #print(mu_lst)
        print(sigama_lst)
        #print(weight_lst)
        break
        
    
    
    
