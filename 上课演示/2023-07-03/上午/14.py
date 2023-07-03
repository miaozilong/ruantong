import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # 设置字体  解决中文乱码
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # x1 = np.arange(1, 50, 2)
    # y1 = x1 ** 2
    # # 给子图取ID  不能重复
    # plt.subplot(221)
    # plt.title('绘图1')
    # plt.plot(x1, y1)
    # plt.subplot(222)
    # plt.title('绘图2')
    # y2 = 1 / x1
    # plt.plot(x1, y2)

    #  使用fig对象加图
    fig = plt.figure(figsize=(10, 6), dpi=100)
    # 间隔的数量会影响图像的质量,  也可以使用np.linspace取指定点的数量
    x = np.arange(0, 3 * np.pi, 1)
    ax1 = fig.add_subplot(223)
    ax1.plot(x, np.sin(x))
    plt.title('绘图3')
    ax2 = fig.add_subplot(224)
    ax2.plot(x, np.cos(x))
    plt.title('绘图4')

    plt.show()
