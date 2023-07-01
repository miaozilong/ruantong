import numpy as np

if __name__ == '__main__':
    n1 = np.array([[1, 2, 3], [4, 5, 6]])
    n2 = np.array([[4, 5, 6], [7, 8, 9]])
    # 矩阵加法
    result = n1 + n2
    # print(result)
    # 矩阵减法
    result = n1 - n2
    # print(result)

    result = n1 * 3
    # print(result)

    n3 = [[1, 2], [3, 4], [5, 6]]
    result = n1.dot(n3)
    # print(result)
    # 使用transpose方法,或者T属性
    result = np.transpose(n3)
    # print(result)

    result = np.linalg.pinv(n3)
    print(result)
