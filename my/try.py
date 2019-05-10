#coding=utf-8

# try catch exception 的用法
try:
    f = open('testfile.txt', 'r', encoding='utf-8')
    print(f.read())
except FileNotFoundError:
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')
finally:
    if f:
        f.close()
