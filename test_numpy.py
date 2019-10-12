
import numpy as np

print("定隔的 arange：固定元素大小间隔")
print(np.arange(8))
print(np.arange(2, 8))
print(np.arange(2, 8, 2))  # arange(start , stop , step) 起点 , 终点 , 间隔; stop 必须要有，start 和 step 没有的话默认为 1


print("定点的 linspace：固定元素个数")
print(np.linspace(2, 6, 3))
print(np.linspace(3, 8, 11)) # linspace (start , stop , num) 起点 , 终点 , 点数；start 和 stop 必须要有，num 没有的话默认为 50

print('创建 默认数组')
print('一维5元素数组 \n', np.zeros(5))    # 标量5代表形状(5,)
print('外2元素内3元素数组 \n', np.ones((2, 3)))  # 有点像 sol
print('外2维，中3维，内4维数组 \n', np.random.random((2, 3, 4)))
print('4维对角矩阵 \n', np.eye(4))
print('k=1 \n', np.eye(4, k=1))
print('k=-1 \n', np.eye(4, k=-1))