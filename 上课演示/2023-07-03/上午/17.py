import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

if __name__ == '__main__':
    print('你好')
    # 设置字体  解决中文乱码
    plt.rcParams['font.sans-serif'] = ['SimHei']
    df = pd.read_excel('出生人口.xlsx')
    print(df)
    x = df['年份']
    y = df['出生人口']
    fig, ax = plt.subplots(figsize=(20, 6))
    # 设置主刻度
    ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
    # 设置副刻度
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
    plt.plot(x, y, color='r', marker='x')
    # 添加标签
    plt.text('1949年', 1275, '建国')
    plt.text('1982年', 2230, '计划生育')
    plt.text('2011年', 1600, '二孩政策')
    plt.show()
