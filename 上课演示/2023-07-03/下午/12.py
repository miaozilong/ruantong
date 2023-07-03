import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # 设置字体为黑体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    x = np.arange(1, 10, 1)
    y = np.arange(1, 10, 1)
    # figsize一般使用4:3或者16:9    dpi  dot per inch
    plt.figure(num='我的第一张图', figsize=(10, 8), dpi=100, facecolor='w')
    # 默认字体是西文字体  需要设置字体为黑体后,才能显示
    plt.title('我的第一张图', {'fontsize': 20})
    plt.xlabel('X轴', {'fontsize': 15})
    plt.ylabel('Y轴', {'fontsize': 15})
    plt.xticks([2, 4, 6, 8])
    # 设置网格线
    plt.grid(axis='y', color='#ccc', linestyle=':', linewidth=1)
    # 画图
    plt.plot(x, y, color="#D2042D", linestyle=":", marker='*')
    # 设置图例
    # loc 'best' 会自动放置图例的位置
    #   'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
    plt.legend(('销量',), fontsize=10, loc="lower right")
    # 显示图像
    plt.show()
