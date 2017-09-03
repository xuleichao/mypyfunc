def search_file(path,file_ext): #  查找所有入院记录以及相应文件的名称
    import os
    dir_name = os.listdir(path) #  获得文件夹中的文件及文件夹
    folder = []
    file = []
    if dir_name != []:
        for name in dir_name: #  遍历所有文件及文件夹，分为文件类和文件夹类
            if '.' not in name:
                folder.append(name)
            else:
                file.append(name)
    else:
        print(path + '是空文件夹')
    if file != []:
        for name in file: #  在文件中寻找以病历记录为开头的html文件
            '''
            first_4str=''
            
            for n in range(4):
                first_4str=first_4str + name[n]
                print(first_4str)
                '''
            if '.' + file_ext in name:
                each_file_path = path + '/' + name
                file_path.append(each_file_path) #  收集找到的文件路径
                inhos_name.append(name)
    if folder != []:
        for folder_name in folder: #  在子文件夹中递归查找
            vir_path = path + '/' + folder_name
            search_file(vir_path) #  递归
    return (file_path,inhos_name)

