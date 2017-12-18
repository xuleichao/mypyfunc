import time

def new():
    tm = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    path = input('your path')
    name = input('your name')
    if path == "''":
        path = ''
        f = open(name + '.py','ab')
        bt = '\'\'\'' + '\n\n' + 'by xlc time:' + tm + '\n' + '\'\'\'' + '\n'
        impt = 'import sys\nsys.path.append(\'D:/mypyfunc\')'
        main_entry = '''if __name__ == \'__main__\':'''
        f.write((bt + impt + '\n\n' + main_entry).encode('utf-8'))
        f.close()
    else:
        f = open(path + '/' + name + '.py','ab')
        bt = '\'\'\'' + '\n\n' + 'by xlc time:' + tm + '\n' + '\'\'\'' + '\n'
        impt = 'import sys\nsys.path.append(\'D:/mypyfunc\')'
        main_entry = '''if __name__ == \'__main__\':'''
        f.write((bt + impt + '\n\n' + main_entry).encode('utf-8'))
        #f.write('\n'.encode('utf-8'))
        #f.write(main_entry.encode('utf-8'))
        f.close()

if __name__=='__main__':
    new()
