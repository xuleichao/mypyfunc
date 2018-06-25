'''

by xlc time:2018-06-04 10:25:57
'''
import sys
sys.path.append('D:/svn_codes/source/public_fun')
import os
main_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
main_path = '/'.join(main_path.split('/')[:-1])
sys.path.append('')
import numpy as np
import pandas as pd
from pandas import DataFrame

class BayesNet:

    def __init__(self, name, cause_nodes, cause_nodes_name, effect_name,\
                 default_F=0.5, read_file=False, root_node=False, init_data=None):
        '''
        name 网络的名字
        cause_nodes 是节点的数量
        read_file 是否从文件中获取网络数据        
        '''
        self.name = name
        self.cause_nodes = cause_nodes
        self.cause_nodes_name = cause_nodes_name
        self.effect_name = effect_name
        self.read_file = read_file
        self.root_node = root_node # 是否初始化根节点
        self.init_data = init_data # 初始化数据
        self.default_F = default_F # 初始默认概率
        self.default_T = 1 - default_F # 初始默认概率
        self.net_init('')
        self.self_detect()
        

    def net_init(self, block_name): # 子网络初始化
        if self.read_file == False: # 是否从文件中获取数据
            self.block_matrix_tf = self.init_tf_block(self.cause_nodes, \
                                                      self.cause_nodes_name)
            
            if self.init_data != None:
                self.init_by_hand(self.block_matrix_tf)
            print(self.block_matrix_tf)
        else:
            pass

    def init_tf_block(self, num=1, name=['target']):#子网真假值的初始化
        if self.root_node == True:
            tf_df = {}
            tf_df[self.effect_name,'F'] = self.default_F
            tf_df[self.effect_name,'T'] = self.default_T
            return DataFrame([tf_df])
        tf_block_scale = 2 ** num
        tf_matrix = []
        for i in range(tf_block_scale):
            b_num = str(bin(i))[2:] # 二进制结果
            if len(b_num) < num:
                for i in range(abs(len(b_num)-num)):
                    b_num = '0' + b_num
            b_num = [int(i) for i in b_num]
            tf_matrix.append(b_num)
        tf_df = DataFrame(tf_matrix, columns=name)
        tf_df[self.effect_name,'F'] = self.default_F
        tf_df[self.effect_name,'T'] = self.default_T
        return tf_df

    def __eval_lst(self, lst0, lst1, string='self.block_matrix_tf'):
        sub_condition = []
        for i in range(len(lst0)):
            sub = '(' + string + '[\'' + lst0[i] + '\']==' + str(lst1[i]) + ')'
            sub_condition.append(sub)
        result = '&'.join(sub_condition)
        return result
    
    def init_by_hand(self, df): # 手动修改网络矩阵值
        data_df_lst = np.array(df).tolist()
        init_data_lst = self.init_data
        new_result = []
        for i in data_df_lst:
            tiny = []
            i_c = i[:-2]
            tiny = tiny + i_c
            for j in init_data_lst:
                j_c = j[:-2]
                if i_c == j_c:
                    tiny = tiny + j[-2:]
                    break
            new_result.append(tiny)
        result = DataFrame(new_result, columns=df.columns)
        self.block_matrix_tf = result

    def self_detect(self): # 自检函数
        '''
        检测概率是否定义错误，之和超过1（报错）, 或小于1（警告）
        '''
        detect_lst = np.array(self.block_matrix_tf).tolist()
        for i in detect_lst:
            sum_add = sum(i[-2:])
            if sum_add > 1:
                print('Probabilty is more than 1', '->',i[-2:])
                raise ValueError
            if sum_add < 1:
                print('Wanning, 概率之和小于1', '->',i[-2:])

def calculate(sub_nodes_cls_lst):
    all_nodes = []
    for i in sub_nodes_cls_lst:
        cause_nodes = i.cause_nodes_name
        effect_nodes = i.effect_name
        all_nodes += cause_nodes
        all_nodes.append(effect_nodes)
    all_nodes = list(set(all_nodes))
    print(all_nodes)
    pass

if __name__ == '__main__':
    A0 = BayesNet('', 0, [], '病史', default_F=0.6, root_node=True)
    A1 = BayesNet(name='', cause_nodes=1, cause_nodes_name=['病史'], effect_name='增加可能性', init_data=[[0, 0.1, 0.9], [1, 0.4, 0.6]])
    A2 = BayesNet('', 2, ['检查', '检验'], '是否符合')
    A3 = BayesNet('', 2, ['增加可能性', '是否符合'], '诊断结果')
    '''
    先获得各个节点，初始节点，互相节点
    待求概率 -> 计算
    '''
    calculate([A0, A1, A2, A3])
