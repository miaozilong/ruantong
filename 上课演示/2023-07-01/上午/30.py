import numpy as np

if __name__ == '__main__':
    n1 = np.array([0, 30, 45, 60, 90])
    # 根据角度求弧度
    # n2 = np.pi * n1 / 180
    # print(n2)
    n2 = np.deg2rad(n1)
    print(n2)
    # 求sin cos tan....
    result = np.sin(n2)
    result = np.cos(n2)
    result = np.tan(n2)
    # print(result)
    # 根据弧度求角度
    result = np.rad2deg(n2)
    print(result)

    sqrt = np.sqrt(result)
    print(sqrt)
    # 参考29页进行测试

