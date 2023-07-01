import numpy as np

if __name__ == '__main__':
    n1 = np.array([[1, 2, 3, ], [4, 5, 6]])  # 2*3
    n2 = np.array([[4, 5, 6, ], [7, 8, 9]])  # 2*3   3*2
    n3 = n1 + n2
    n3 = n1 - n2
    # 数乘
    n3 = n1 * 3
    # 转置n2
    n2t = n2.T
    # 点乘
    n3 = n1.dot(n2t)
    # print(n3)
    # 转置
    # print(n2)
    # print(n2t)
    # 也可以使用transpose方法
    n2t = n2.transpose()
    # print(n2t)

    # 求逆
    pinv = np.linalg.pinv(n1)
    print(pinv)
