# 打平 flatten
a = [1, 2, [3, 4], [[5, 6], [7, 8]]]

fn = lambda x: [y for l in x for y in fn(l)] if type(x) is list else [x]

b = fn(a)

print(b)

# 查看对象的 属性和 方法 (两种方式)
print(dir(b))

print(help(b))

import decimal
from decimal import Decimal

print(dir(decimal))
print(help(decimal))

print(decimal.getcontext())

t = (1, 2, 3, 4, 5)
a, b, *_, c = t
print(a, b, c)
print(_)

# 判断某数据类型是否可以更改 (两种方式) id() 和 hash()

# 集合 set (直接`{}`定义，或者将 list 和 tuple转换成 set)

set1 = {1, 5, 6}
set2 = set([1, 8, 9])
set3 = set((4, 5, 3))

set11 = {1, 1, 5, 6}
set22 = set([1, 1, 8, 7])
set33 = set((4, 4, 8, 9))

print(set1)
print(set2)
print(set3)
print(set11)
print(set22)
print(set33)

# set 的一些骚操作

setA = {4, 8, 9}
setB = {8, 6, 7}

'''
并集
'''

unionSet1 = setA | setB
unionSet2 = setA.union(setB)

print('并集')
print(unionSet1)
print(unionSet2)

'''
交集
'''

inSet1 = setA & setB
inSet2 = setA.intersection(setB)

print('交集')
print(inSet1)
print(inSet2)

'''
差集 
'''

deSetA1 = setA - setB
deSetA2 = setA.difference(setB)

deSetB1 = setB - setA
deSetB2 = setB.difference(setA)

print('差集')
print(deSetA1)
print(deSetA2)
print(deSetB1)
print(deSetB2)


'''
对称差集 XOR (即: 清除掉交集部分的并集)
'''

symDeSetA1 = setA ^ setB
symDeSetA2 = setA.symmetric_difference(setB)

symDeSetB1 = setB ^ setA
symDeSetB2 = setB.symmetric_difference(setA)

print('对称差集 XOR')
print(symDeSetA1)
print(symDeSetA2)
print(symDeSetB1)
print(symDeSetB2)

#  for

arr = [4, 8, 7, 9, 6, 5]

# 无 索引的 for
for a in arr:
    print(a)

# 有 索引的 for
for i, a in enumerate(arr):
    print(i, a)

