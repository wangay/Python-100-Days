# coding=utf-8

"""
file操作


"""

# 直接读取. 需要加try catch ,关闭流
import base64

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

# with 更简单的做法, 避免上面try . 一次性读取整个文件内容
with open('致橡树.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# 通过for-in循环逐行读取
with open('致橡树.txt', mode='r') as f:
    for line in f:
        print(line, end='')
        # time.sleep(0.5)
print()


# 读取文件按行读取到列表中
with open('致橡树.txt') as f:
    lines = f.readlines()
print(lines)

# 写入文件# # # # # # # ## # # # # # # ## # # # # # # ## # # # # # # #
# 试一试有什么不一样#
# 没有这个文件prime.txt的话,会自动在当前路径创建.
# with open('prime.txt', 'a') as f:
with open('prime.txt', 'w') as f:
    for num in range(2, 100):
        f.write(str(num) + '\n')
print('写入完成!')


# 二进制数据 (图片等) 读取,写入# # # # # # # ## # # # # # # ## # # # # # # ## # # # # # # #
#  r:read w:write  b:binary 二进制
with open('mm.jpg', 'rb') as f:
    data = f.read()
    # print(type(data))
    # print(data)
    print('字节数:', len(data))
    # 将图片处理成BASE-64编码
    print(base64.b64encode(data))

with open('girl.jpg', 'wb') as f:
    f.write(data)
print('写入完成!')
