import numpy as np

if __name__ == '__main__':
    # 随机整数,最小是10,最大是200(不包含)  形状是5*6
    n1 = np.random.randint(10, 200, (5, 6))
    print(n1)
    print("最小值", np.min(n1))
    print("最大值", np.max(n1))
    print("0轴最小值", np.amin(n1, 0))
    print("求和", np.sum(n1))
    print("求极差", np.ptp(n1))
    print("求中位数", np.median(n1))
    print("求平均数", np.mean(n1))
    # 附加:  求加权平均数
    print("标准差", np.std(n1))

