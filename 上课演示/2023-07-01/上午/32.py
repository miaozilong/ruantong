import numpy as np

if __name__ == '__main__':
    n1 = np.random.randint(200, size=(6, 5))
    print(n1)
    print("最小值", np.min(n1))
    print("最大值", np.max(n1))
    print("求和", np.sum(n1))
    print("求极值", np.ptp(n1))
    print("中位数", np.median(n1))
    print("平均值", np.mean(n1))
    # 附加题: 求加权平均值
    print("标准差", np.std(n1))
