import random
import time
import numpy as np

if __name__ == '__main__':
    ndarray = np.random.randint(10, 100, 8)
    print(ndarray)
    # 默认按行进行重组
    # ndarray = ndarray.reshape((2, 4))
    # print(ndarray)
    ndarray = ndarray.reshape((2, 4), order='F')
    print(ndarray)

    print()
