import numpy as np


"""
数组
"""
a = np.array([
    [1,2],
    [3,4]
])
# 矩阵点乘,对应位置的数据相乘
b1 = a*a
# print(b1)
# 矩阵点乘,对应位置的数据相乘
b2 = np.multiply(a, a)
# print(b2)

# 矩阵乘法,真正的矩阵乘法
b3 = np.dot(a, a)
# print(b3)


"""
矩阵
"""
A = np.mat([[1,2],
           [3,4]])

# 矩阵点乘,和数组中的矩阵乘法一样
B1 = A*A
# print(B1)
# 对应位置相乘
B2 = np.multiply(A, A)
# print(B2)

# 矩阵点乘,和数组中的矩阵乘法一样
B3 = np.dot(A, A)
# print(B3)


A2 = np.linalg.pinv(A)
B4 = A2*A
# print(B4)

B5 = A.I

print(A * B5)

a6 = np.eye(2,2)
print(a6)