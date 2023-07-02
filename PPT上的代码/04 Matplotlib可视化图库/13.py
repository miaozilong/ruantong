import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x1 = np.arange(1, 10, 2)
    y1 = np.linspace(10, 20, 5)
    # 正常显示中文标签  设置为黑体
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # 设置画布尺寸、分辨率、背景颜色
    # dpi可以使用10和150 演示看一下  edgecolor='#f00'看不出来  不演示了
    plt.figure(num='我的第一张折线图', figsize=(10, 6), dpi=100, facecolor='#0f0', frameon=True)

    plt.title('我的第一张折线图', {'fontsize': 15, 'va': 'bottom'}, pad=3, color='#00f')

    plt.xlabel('X轴', {'fontsize': 15, 'va': 'bottom'})
    plt.ylabel('Y轴')

    plt.xticks([2, 4, 6, 8])
    # 设置网格线，linewidth设置宽度，axis='x'设置隐藏和x轴平行的网格线
    plt.grid(color='#191970', linestyle=':', linewidth=1, axis='y')

    plt.plot(x1, y1, color='#f00', linestyle='-', marker='x')
    # 设置图例，loc设置图例显示位置  loc随便写一个 看看可以写什么
    plt.legend(('图例',), loc='best', fontsize=10)

    plt.show()
