'''

by xlc time:2018-12-21 08:49:19
'''
import sys
#sys.path.append('D:/svn_codes/source/public_fun')
import os
main_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
main_path = '/'.join(main_path.split('/')[:-1])
from matplotlib import pyplot as plt
import json

if __name__ == '__main__':
    f = open('EM_rslt.txt', 'r', encoding='utf-8').readlines()
    data = [json.loads(i) for i in f]
    X = [i[0][0] for i in data]
    y = [i[0][1] for i in data]
    sym = [i[1][0].split('_')[0] for i in data]
    ax = plt.figure().add_subplot(111)
    for i in range(len(X)):
        if sym[i] == '1':
            ax.scatter(X[i], y[i], color='black')
        elif sym[i] == '0':
            ax.scatter(X[i], y[i], color='red')
        else:
            ax.scatter(X[i], y[i], color='blue')
    plt.show()
