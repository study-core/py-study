
# 默认函数一定要放在位置参数后面，不然程序会报错


def defualt_args(id, nlt = 1):
    """
    默认参数 必须放结尾
    :param id:
    :param nlt:
    :return:
    """
    print(id, nlt)

def instrument4( id, ntl=1, curR='CNY', *args ):
    """
    可变参还要写在最后面
    *args - 可变参数，可以是从零个到任意个，自动组装成元组
    :param id:
    :param ntl:
    :param curR:
    :param args:
    :return:
    """
    pv = 0
    for n in args:
        pv = pv + n
    print('id:', id)
    print('notional:', ntl)
    print('reporting currency:', curR)
    print('present value:', pv*ntl)


dcf = (1, 2, 3, 4, 5)
# 前面加个通配符 * 是拆散元组，把元组的元素传入函数中
instrument4('MM1001', 10, 'EUR', *dcf)


def instrument5(id, ntl=1, curr='CNY', *args, **kw):
    """
    关键字 参数还要放到最后面
    **kw - 关键字参数，可以是从零个到任意个，自动组装成字典
    :param id:
    :param ntl:
    :param curr:
    :param args:
    :param kw:
    :return:
    """
    pv = 0
    for n in args:
        pv = pv + n

    print('id:', id)
    print('notional:', ntl)
    print('reporting currency:', curr)
    print('present value:', pv*ntl)
    print('keyword:', kw)


#  不传入任何「关键字参数」，kw 为空集
instrument5('MM1001', 100, 'EUR', 1, 2, 3)

# 传入 k-v
instrument5('MM1001', 100, 'EUR', 1, 2, 3, dc='act/365', ctp='GS')


def instrument6(id, ntl=1, curr='CNY', *, ctp, **kw):

    """
    命名关键字参数

    ctp 就是 命名关键字参数 `*, ctp` 他们是一个整体
    :param id:
    :param ntl:
    :param curr:
    :param ctp:
    :param kw:
    :return:
    """
    print('id:', id)
    print('notional:', ntl)
    print('reporting currency:', curr)
    print('counterparty:', ctp)
    print('keyword:', kw)


# ctp 是「命名关键字参数」，而 dc 是「关键字参数」
instrument6('MM1001', 100, 'EUR', dc='act/365', ctp='GS')

"""
在 Python 中定义函数，可以用位置参数、默认参数、可变参数、命名关键字参数和关键字参数，
这 5 种参数中的 4 个都可以一起使用，但是注意，参数定义的顺序必须是：

  - 位置参数、默认参数、可变参数 和 关键字参数。
  - 位置参数、默认参数、命名关键字参数 和 关键字参数。
  
  - 可变参数和命名关键字参数是互斥的 ？

要注意定义可变参数和关键字参数的语法：

*args 是可变参数，args 接收的是一个 tuple
**kw 是关键字参数，kw 接收的是一个 dict

命名关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。定义命名关键字参数不要忘了写分隔符 *，否则定义的是位置参数
"""



# 高阶内置函数
#
# map, filter 和 reduce

lst = [1, 2, 3, 4, 5]
map_iter = map(lambda x: x**2, lst)

#  map_iter 是 map 函数的返回对象 (它是一个迭代器)
print("map func")
print(map_iter)
print(list(map_iter))

print("reduce func")
from functools import reduce
print("reduce 遍历叠加 list 所有元素", reduce(lambda x, y: x+y, lst))
print("基于一个基础值，再遍历叠加 list 的元素", reduce(lambda x, y: x+y, lst, 100))


filter_iter = filter(lambda n: n % 2 == 1, lst)
print("filter func")
#  filter_iter 是 filter 函数的返回对象 (它是一个迭代器)
print(filter_iter)
print(list(filter_iter))

# 偏函数
#
#  主要是把一个函数的参数 (一个或多个) 固定下来
#  用于专门的应用上

#  定义降序 函数
lst = [3, 1, 2, 5, 4]
arr = sorted(lst)
print("默认排序")
print(arr, lst)


from functools import partial
# 入参为 sorted函数 和 指定sorted函数的 reverse参数为true
sorted_dec = partial(sorted, reverse=True)
arr = sorted_dec(lst)
print("偏函数自定义降序")
print(arr, lst)


# 柯里化
#
# 将原来接收 2 个参数的函数 f(x, y) 变成新的接收 1 个参数的函数 g(x) 的过程
# 其中新函数 g = f(y)

def add1(x, y):
    return x + y


# 柯里化
def add2(x):
    def add(y):
        return x + y
    return add


g = add2(2)

print("柯里化")
print(add1(2, 3))
print(add2(2)(3))
print(g(3))


# 解析式

'''
# list comprehension
[值 for 元素 in 可迭代对象 if 条件]
# dict comprehension
{键值对 for 元素 in 可迭代对象 if 条件}
# set comprehension
{值 for 元素 in 可迭代对象 if 条件} 
'''


lst = [1, 2, 3, 4, 5]
# 情况1
odds = []
for n in lst:
    if n % 2 == 1:
        odds.append(n * 2)
print("常规迭代 list 情况1", odds)

# 情况2
odds = [n * 2 for n in lst if n % 2 == 1]
print("解析式迭代 list 情况2", odds)

#  double for
lst = [[1, 2], [2, 5, 3], [8, 9]]

flattened = []
for row in lst:
    for n in row:
        flattened.append(n)

print("常规双层for迭代", flattened)

flattened = [n for row in lst for n in row]
print("解析式双层for迭代", flattened)