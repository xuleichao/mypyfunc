'''
## dataset_util
by xlc time:2018-12-20 08:28:17
'''
import sys
#sys.path.append('D:/svn_codes/source/public_fun')
import os
import matplotlib.pyplot as plt  
import numpy as np  
from sklearn.cluster import KMeans
from sklearn import datasets

def load_data():
    iris = datasets.load_iris()['data']
    X = iris[:, 2:4] ##表示我们只取特征空间中的后两个维度
    return X
