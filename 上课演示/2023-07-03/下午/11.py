import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.arange(1, 10, 1)
    y = np.arange(1, 10, 1)
    # 画图
    plt.plot(x, y, color="#D2042D", linestyle=":", marker='*')
    # 显示图像
    plt.show()
