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
def NNtrain(X, y, nnHid_scale, num_passes=2000, study_rate=0.01): #神经网络模型训练
    X_num = len(X) #特征的个数
    y_num = len(y) #标记集的个数
    '''
    1. 先算隐层输入，2. 然后算隐层输出，
    3. 然后算输出层输入，4. 然后算输出层输出，
    5. 获得损失，然后更新各个参数
    '''
    Wt_I = np.ones(X_num, nnHid_scale)#输入层权重
    Gate_H = np.zeros(nnHid_scale)#隐层的阈值
    Wt_H = np.ones(nnHid_scale, y_num)#隐层的权重
    Gate_O = np.zeros(y_num)#输出层的阈值

    
if __name__ == '__main__':
    # 制作散点图，数据集
    np.random.seed(0)
    X, y = sklearn.datasets.make_moons(200, noise=0.2)
    
