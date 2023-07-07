# 一元线性拟合
import numpy as np
import matplotlib.pyplot as plt
# 构造原始数据集
x = np.arange(0,10)
y = np.random.rand(10)*2
# 打印随机数据集点对
print(list((i,j) for (i,j) in zip(x,y)))
# 根据一元线性回归y=ax+b的最小二乘法待定系数公式求系数a和b
t1=t2=t3=t4=0
n = len(x)
for i in range(n):
    t1 += y[i]
    t2 += x[i]
    t3 += x[i] * y[i]
    t4 += x[i] ** 2
    a = (t1*t2/n - t3) / (t2*t2/n - t4)
    b = (t1 - a*t2) / n
    #绘制拟合曲线和样本点
    plt.plot(x,y,'o',label='Original data',markersize=2)
    plt.plot(x, a*x + b, 'r', label='Fitted line')
plt.show()