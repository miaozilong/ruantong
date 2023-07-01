import numpy as np

if __name__ == '__main__':
    # 构建numpy数据
    # 构建一维数据
    l = [1, 2, 3]
    ndarray = np.array(l)
    ndarray = np.array([[1, 2, 3], [4, 5, 6]])
    # 打印形状
    print(ndarray.shape)
    # 打印维度
    print(ndarray.ndim)
    # 打印元素个数
    print(ndarray.size)
    # 打印类型
    print(ndarray.dtype)
