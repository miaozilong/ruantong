import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x1 = np.arange(1, 10, 2)
    y1 = np.linspace(10, 20, 5)
    # 颜色要讲一讲  https://www.runoob.com/html/html-colors.html
    plt.plot(x1, y1, color='#f00', linestyle='-', marker='x')
    plt.show()
