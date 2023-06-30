import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['simsun']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

if __name__=="__main__":
    # 折线图--表示虚线:表示点线color标识颜色
    s=np.array([1,2,3,4,5,6])
    plt.plot(s,s,'-',color='#f00')
    plt.show()
