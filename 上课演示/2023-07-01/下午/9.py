# 1. 安装pip install numpy -i  https://pypi.tuna.tsinghua.edu.cn/simple
# 2. 引入numpy
import numpy as np

if __name__ == '__main__':
    # python中的列表
    # l = [1, 2, 3]
    l = [[1, 2, 3], [4, 5, 6]]
    n1 = np.array(l)
    print(n1)
    # 类型为numpy.ndarray类型           计算速度,比python的列表的计算速度大概快2个数量级
    print(type(n1))
    # 形状
    print(n1.shape)
    # 维度
    print(n1.ndim)
    # 元素的数量
    print(n1.size)
    # 每个元素所占的字节    了解
    print(n1.itemsize)
    # 元素的类型   整数类型是int32     numpy中不要混放类型
    print(n1.dtype)
