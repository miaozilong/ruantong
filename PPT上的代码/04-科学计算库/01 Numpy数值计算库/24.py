import random
import time
import numpy as np

if __name__ == '__main__':
    n1 = np.linspace(1, 10, 6, dtype='int').reshape(2, 3)
    n2 = np.linspace(10, 20, 6, dtype='int').reshape(2, 3)
    # 矩阵加法
    result = np.add(n1, n2)
    # 矩阵减法
    result = np.subtract(n1, n2)
    # 数乘
    result = n1 * 5
    result = 5 * n1
    # 点乘
    result = np.dot(n1, np.reshape(n2, (3, 2)))

    print()
