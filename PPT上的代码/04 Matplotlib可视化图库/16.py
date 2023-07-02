import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.ticker as ticker

# https://zhuanlan.zhihu.com/p/94118835
if __name__ == '__main__':
    df = pd.read_excel('出生人口.xlsx')
    print(df)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    x1 = df['年份']
    y1 = df['出生人口']
    ax = plt.axes()
    # 主刻度
    ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
    # 副刻度
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    plt.plot(x1, y1, color='#f00', linestyle='-', marker='x')

    # 在图上增加文字标签
    style = dict(size=10, color='gray')
    plt.text('1949年', 1275, '建国', **style)
    plt.text('1980年', 1776, '独生子女政策', **style)
    plt.text('2011年', 1600, '二孩政策', **style)

    plt.show()
