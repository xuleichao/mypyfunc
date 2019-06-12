import itertools
import pandas as pd

def get_product(lst):
    result = itertools.product(lst, repeat=len(lst))
    new = []
    for i in result:
        if len(set(i)) == len(a):
            new.append(i)
    return new

def lst_utils(lst):
    # 对一个list 做标记
    # ['a', 'b', 'c'] -> [[0, 'a'], [1, 'b'], [2, 'c']]
    return list(zip(range(len(lst)), lst))

def comb_utils(lst, group_num):
    # 对一个list 进行组合分组
    length = len(lst)
    comb_rslt = itertools.combinations(range(1, len(lst)-1), group_num)
    return comb_rslt

def comb_rslt_utils(lst, comb_rslt):
    # 对组合结果进行处理
    result = []
    comb_rslt = [list(i) for i in comb_rslt]
    for comb in comb_rslt:
        comb.insert(0, 0)
        comb.append(len(lst))
        #print(comb)
        mid_group = []
        for ln in range(len(comb)-1):
            group = lst[comb[ln]: comb[ln+1]]
            #print(group)
            mid_group.append(set(group))
        result.append(mid_group)
    return result

def drop_duplicates(result_lst):
    # 对结果进行去重操作
    result_lst = [[tuple(sorted(j)) for j in i] for i in result_lst]
    result_lst = [sorted(j, key=lambda x:x[0]) for j in result_lst]
    df_lst = pd.DataFrame(result_lst).drop_duplicates().values.tolist()
    return df_lst
                    

def comb_main(a, group_num):
    lst = get_product(a)
    rslt_lst = []
    for i in lst:
        comb_rslt = comb_utils(i, group_num-1)
        result = comb_rslt_utils(i, comb_rslt)
        rslt_lst += result
        #break
        rslt_lst += result
    drop_rslt = drop_duplicates(rslt_lst)
    return drop_rslt
    
if __name__ == '__main__':
    a = [1,2,3,4,5]
    group_num = 4
    rslt = comb_main(a, group_num)
    
    
