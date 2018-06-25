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
def visualize(X, y, model):

    # plt.scatter(X[:, 0], X[:, 1], s=40, c=y, cmap=plt.cm.Spectral)

    # plt.show()

    plot_decision_boundary(lambda x:predict(model,x), X, y)

    plt.title("Logistic Regression")

def plot_decision_boundary(pred_func, X, y):

    # Set min and max values and give it some padding

    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5

    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

    h = 0.01

    # Generate a grid of points with distance h between them

    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Predict the function value for the whole gid

    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])

    Z = Z.reshape(xx.shape)

    # Plot the contour and training examples

    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)

    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)

    plt.show()

def sigmoid(lst):
    y = 1/(1 + np.exp(-lst))
    return y

def predict(x, model):
    W_input, W_hid, yuzhi_hid, yuzhi_out = model[0], model[1], model[2], model[3]
    Hid_out = sigmoid(np.dot(W_input, x.reshape(-1, 1)) - yuzhi_hid)#隐层输出
    Out_out = sigmoid(np.dot(W_hid, Hid_out) - yuzhi_out)#输出层输出
    return np.argmax(Out_out, axis=0), Out_out

def NNtrain(X, y, nnHid_scale, num_passes=2000, study_rate=0.01): #神经网络模型训练
    X_num = X.shape[1] #特征的个数
    y_num = y.shape[1] #标记集的个数
    '''
    1. 先算隐层输入，2. 然后算隐层输出，
    3. 然后算输出层输入，4. 然后算输出层输出，
    5. 获得损失，然后更新各个参数
    '''
    W_input = np.random.randn(nnHid_scale, X_num) #输入端的权重
    W_hid = np.random.randn(y_num, nnHid_scale) #隐层的权重
    yuzhi_hid = np.random.randn(nnHid_scale, 1) #隐层的阈值
    yuzhi_out = np.random.randn(y_num, 1) #输出的阈值

    for i in range(num_passes): #迭代更新
        all_loss = []
        for x in range(X.shape[0]):
            x_input = X[x].reshape(-1, 1) #x input
            y_out = y[x].reshape(-1, 1) #y out
            Hid_out = sigmoid(W_input.dot(x_input) - yuzhi_hid)#隐层输出
            Out_out = sigmoid(W_hid.dot(Hid_out) - yuzhi_out)#输出层输出
            #开始更新
            G = Out_out * (1 - Out_out) * (y_out - Out_out) #
            delta_W_hid = study_rate * G.dot(Hid_out.reshape(1, -1))# 隐层权重的增量
            delta_yuzhi_out = -study_rate * G#输入端阈值更新增量
            E = Hid_out * (1 - Hid_out) * np.dot(W_hid.T, G)#
            delta_W_input = study_rate * (E.dot(\
                            np.array(x_input).reshape(1, -1))) #输入端权重更新增量
            delta_yuzhi_hid = -study_rate * E#隐层阈值更新增量
            #权重阈值更新
            W_hid = W_hid + delta_W_hid
            yuzhi_out = yuzhi_out + delta_yuzhi_out
            W_input = W_input + delta_W_input
            yuzhi_hid = yuzhi_hid + delta_yuzhi_hid
            loss = 0.5 * sum(np.power((Out_out - y_out), 2))
            all_loss.append(loss)
        #loss
        min_loss = sum(all_loss)/(X.shape[0])
        print(min_loss)
    return [W_input, W_hid, yuzhi_hid, yuzhi_out]


    
if __name__ == '__main__':
    # 制作散点图，数据集
    np.random.seed(0)
    X, y = sklearn.datasets.make_moons(200, noise=0.20)
    r = []
    for i in y:
        if i==0:
            r.append([0, 1])
        else:
            r.append([1, 0])
    r = np.array(r)
    model = NNtrain(X, r, nnHid_scale=6, num_passes=2000, study_rate=0.1)
    result = []
    for i in X:
        result.append(predict(i.reshape(-1, 1), model)[0])
    y2 = np.array(result).T
    t = np.array([i.tolist()[0] for i in result])
    plt.scatter(X[:, 0], X[:, 1], s=40, c=t, cmap=plt.cm.Spectral)
    #plt.scatter(X[:, 0], X[:, 1], s=40, c=y, cmap=plt.cm.Spectral)
    plt.show()
    
    
