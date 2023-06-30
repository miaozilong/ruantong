import random
import time
import numpy as np

if __name__ == '__main__':
    ndarray = np.array([[1, 2, 3], [4, 5, 6]])
    ndarray = np.zeros((2, 4))
    ndarray = np.ones((3, 2, 4))
    ndarray = np.eye(4, 3)
    # 尽量少用 容易出问题
    ndarray = np.empty((2, 3))
    ndarray = np.full((2, 3), '1')
    ndarray = np.arange(10, 30, 3)
    ndarray = np.linspace(10, 100, 3)
    ndarray = np.logspace(0, 9, 11, base=2)
    # 数量为3的以为数组，数据为0到1
    ndarray = np.random.rand(3)
    # 随机二维数组
    ndarray = np.random.rand(3, 4)
    ndarray = np.random.randn(300)
    # 生成10到12的随机矩阵 不包含13  和python不一致  要注意下
    ndarray = np.random.randint(10, 13, size=(5, 10))
    ndarray = np.random.randint(10, 100, 8)

    print()
