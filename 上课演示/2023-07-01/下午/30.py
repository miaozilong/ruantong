import numpy as np

if __name__ == '__main__':
    n1 = np.array([0, 30, 45, 60, 90])
    # 角度转换成弧度
    # n2 = np.pi * n1 / 180
    # print(n2)
    n2 = np.deg2rad(n1)
    print(n2)
    sin = np.sin(n1)
    print(sin)
    sqrt = np.sqrt(n1)
    print(sqrt)
    # 参考P29
