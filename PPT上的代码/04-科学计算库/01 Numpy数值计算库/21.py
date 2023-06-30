import random
import time
import numpy as np

if __name__ == '__main__':
    ndarray1 = np.array([1, 2, 3])
    ndarray2 = np.array([4, 5, 6])
    # 横向扩展
    hstack = np.hstack((ndarray1, ndarray2))
    # 纵向扩展
    vstack = np.vstack((ndarray1, ndarray2))
    # 删除数据
    ndarray = np.delete(vstack, 1, axis=1)
    # 修改数据
    ndarray[0][1] = 8

    ndarray = ndarray[:, 1:]

    # numpy.where()
    # 有两种用法：
    # 1. np.where(condition, x, y)  满足条件(condition)，输出x，不满足输出y。
    a1 = np.arange(10)
    n1 = np.where(a1 > 5, 1, -1)
    #  2. 只有条件 (condition)，没有x和y，则输出满足条件 (即非0) 元素的坐标 (等价于numpy.nonzero)。这里的坐标以tuple的形式给出，通常原数组有多少维，输出的tuple中就包含几个数组，分别对应符合条件元素的各维坐标。
    a1 = np.reshape(a1, (2, 5))
    n1 = np.where(a1 > 5)

    print()
