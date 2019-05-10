# 测试list的常用
fruits = ['e1', 'e2', 'e3', 'e4','e5','e6']
print(fruits)
# 通过下标访问元素
print(fruits[0])
print(fruits[1])

# 最后一个值
print(fruits[-1])

# 最后第二个值
print(fruits[-2])

# 添加元素append
fruits.append('pitaya')

# 添加元素insert . 在index的位置放上元素
fruits.insert(0, 'banana')

print(fruits)

# 删除元素
del fruits[0]
print(fruits)

# 删除元素 pop  最后一个
fruits.pop()
print(fruits)

# 删除元素 remove  指定的值
fruits.remove('e1')
print(fruits)

# 循环遍历列表元素
for fruit in fruits:
    print(fruit)
    # print 默认是换行,否则指定end不是\n ,用""
    # print(fruit, end=' ')


# 列表切片 .取部分值 . 前闭后开
fruits2 = fruits[1:3]
print(fruits2)

fruits4 = fruits[-3:-1]
print(fruits4)

# 取最后一个值
print(fruits[-1])

# 取最后数,第二个值
print(fruits[-2])

# 用range创建数值列表
list1 = list(range(1, 11))
print(list1)

# 生成表达式. 对每一个x, 获得它的平方作为一个元素.
list2 = [x * x for x in range(1, 11)]
print(list2)

# 表达式. m+n作为一个元素. 第一个为A1,第二个 A2
list3 = [m + n for m in 'ABCDEFG' for n in '12345']
print(list3)

# 同上. 变为小括号. 不是list,而是生成器.
gen = (m + n for m in 'ABCDEFG' for n in '12345')
print(gen)
for elem in gen:
    print(elem, end=' ')