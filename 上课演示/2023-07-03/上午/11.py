import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # 设置字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    x = np.arange(1, 10, 2)
    y = np.arange(1, 10, 2)

    # figsize 图像的大小
    # dip   图像密度
    plt.figure(num='我的示例图', figsize=(20, 12), dpi=100, facecolor='#50C878')
    # 默认使用的是西方字体
    plt.title('我的示例图', {'fontsize': 20}, color='#00f')
    plt.xlabel('X轴', {'fontsize': 15})
    plt.ylabel('Y轴', {'fontsize': 15})
    # 设置x轴的刻度
    plt.xticks([2, 4, 6, 8])
    # 设置网格线
    plt.grid(axis='y', color='#00BFFF', linestyle=':')
    plt.plot(x, y, color='r', linestyle='solid', marker='*')
    plt.legend(("销量",), fontsize=10, loc='upper left')
    plt.show()
