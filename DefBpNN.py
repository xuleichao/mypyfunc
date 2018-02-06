'''
To write a neutral net(NN) by BP Augorithm. And define a
common function of NN for later using.
by xlc time:2018-02-01 21:37:28
'''
import sys
sys.path.append('G:/Github_codes/mypyfunc')
import sklearn.datasets
import numpy as np
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt

#X: 特征集，y: 标记集
#nnHid_scale: 隐层的个数
#num_passes: 训练次数上限
#study_rate: 学习率
def sigmoid(lst):
    y = 1/(1 + np.exp(lst))
    return y

def NNtrain(X, y, nnHid_scale, num_passes=2000, study_rate=0.01): #神经网络模型训练
    X_num = X.shape[1] #特征的个数
    y_num = 1 #标记集的个数
    '''
    1. 先算隐层输入，2. 然后算隐层输出，
    3. 然后算输出层输入，4. 然后算输出层输出，
    5. 获得损失，然后更新各个参数
    '''
    W_input = np.ones((X_num, nnHid_scale)) #输入端的权重
    W_hid = np.ones((nnHid_scale, y_num)) #隐层的权重
    yuzhi_hid = np.zeros(nnHid_scale) #隐层的阈值
    yuzhi_out = np.zeros(y_num) #输出的阈值

    for i in range(num_passes): #迭代更新
        for x in range(X.shape[0]):
            Hid_out = sigmoid(X[x].dot(W_input) - yuzhi_hid)#隐层输出
            Out_out = sigmoid(Hid_out.dot(W_hid) - yuzhi_out)#输出层输出
            #开始更新
            G = Out_out * (1 - Out_out) * (np.array(y[x]) - Out_out) #
            delta_W_hid = study_rate * Hid_out.reshape(nnHid_scale, -1).dot(G) # 隐层权重的增量
            delta_yuzhi_out = -study_rate * G#输入端阈值更新增量
            E = Hid_out * (1 - Hid_out) * np.dot(W_hid, G)#
            delta_W_input = study_rate * (E.reshape(nnHid_scale, -1)\
                            * np.array(X[x]).reshape(-1, X_num)).T #输入端权重更新增量
            delta_yuzhi_hid = -study_rate * E#隐层阈值更新增量
            #权重阈值更新
            W_hid = W_hid + delta_W_hid.reshape(nnHid_scale, -1)
            yuzhi_out = yuzhi_out + delta_yuzhi_out
            W_input = W_input + delta_W_input
            yuzhi_hid = yuzhi_hid + delta_yuzhi_hid
    return [W_input, W_hid, yuzhi_hid, yuzhi_out]
    
if __name__ == '__main__':
    # 制作散点图，数据集
    np.random.seed(0)
    X, y = sklearn.datasets.make_moons(200, noise=0.2)
    print(NNtrain(X, y, 3))
    
