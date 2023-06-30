import numpy as np

if __name__ == '__main__':
    n1 = np.array([0, 30, 45, 60, 90])
    n2 = n1 * np.pi / 180
    n2 = np.deg2rad((n1))
    result = np.sin(n2)
    result = np.cos(n2)
    result = np.tan(n2)

    # 求角度
    n3 = np.degrees(n2)

    n4 = np.arange(1, 10, 3)
    n5 = np.sqrt(n4)
    n6 = np.square(n4)
    n7 = np.power(n4, 3)

    print()
