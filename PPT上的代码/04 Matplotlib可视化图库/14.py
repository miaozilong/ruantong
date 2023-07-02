import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']
    x1 = np.arange(1, 50, 2)
    y1 = x1 * x1
    plt.subplot(221)
    plt.title('绘图1')
    plt.plot(x1, y1)
    plt.subplot(222)
    plt.title('绘图2')
    plt.plot(x1, 1 / x1)


    fig = plt.figure(figsize=(10, 6), dpi=100)
    x2 = np.arange(0, 3 * np.pi, 0.1)
    ax1 = fig.add_subplot(223)
    ax1.plot(x2, np.cos(x2))
    plt.title('绘图3')

    ax2 = fig.add_subplot(224)
    plt.title('绘图4')
    ax2.plot(x2, np.cos(x2))

    plt.show()
