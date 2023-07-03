import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    # 设置字体为黑体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 使用pandas读取文件
    df = pd.read_excel('出生人口.xlsx')
    print(df)
    x = df['年份']
    y = df['出生人口']
    plt.figure(figsize=(20, 6), dpi=100)
    # 设置X轴的密度
    ax = plt.axes()
    # 每10年,设置一个主刻度
    ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
    # 每1年,设置一个副刻度
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    plt.grid(color='#D3D3D3', axis='y')
    plt.plot(x, y, color='#f00', marker='o')
    plt.text('1949年', 1275, '建国')
    plt.text('1961年', 949, '三年灾害')
    plt.text('1982年', 2230, '计划生育')
    plt.text('2016年', 1786, '全面二孩政策')
    plt.show()
