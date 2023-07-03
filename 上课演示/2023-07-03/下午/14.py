import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # 设置字体为黑体
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # 方法1 使用subplot
    # x = np.arange(0, 50, 2)
    # y1 = x * x
    # y2 = 1 / x
    # # 指定子图的编号 subplot
    # plt.subplot(221)
    # plt.title('抛物线')
    # plt.plot(x, y1)
    # plt.subplot(222)
    # plt.title('双曲线')
    # plt.plot(x, y2)

    # 方法2  在画布上使用add_subplot()方法
    # 如果折线图上点数太少,则曲线会失真
    x = np.linspace(0, 3 * np.pi, 50)
    fig = plt.figure(figsize=(10, 6), dpi=100)
    ax1 = fig.add_subplot(223)
    ax1.plot(x, np.sin(x))
    ax2 = fig.add_subplot(224)
    ax2.plot(x, np.cos(x))
    plt.show()

    # 附加题: 在同一个图上,画4张子图
