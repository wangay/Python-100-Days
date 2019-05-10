# coding=utf-8
"""
set
"""

set1 = {1, 2, 3, 3, 3, 2}
print(set1)

set2 = set(range(1, 10))
print(set2)

# 增加
set1.add(4)
set1.add(5)
print(set1)

# update 会增加11 12
set2.update([11, 12])
print(set2)

# 遍历集合容器
for elem in set2:
    print(elem,end=" ")

# - 交集
# - 并集
# - 差集
# - 子集
# - 超集

set1 = set(range(1, 7))
print(set1)
set2 = set(range(2, 11, 2))
print(set2)
set3 = set(range(1, 5))
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))

