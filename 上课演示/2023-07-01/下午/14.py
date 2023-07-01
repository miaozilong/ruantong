# 三种方式  1. 自动安装,写完代码,光标放到"numpy"上  点击install         2. 按ALT+F12  注意FN功能键  打开控制台 输入pip install -i https://pypi.tuna.tsinghua.edu.cn/simple
#          3. 菜单-file-settings-project-python interpreter 点击包上的+号  输入numpy进行安装
#          如果使用了虚拟环境,不要直接在cmd上直接安装
import numpy as np

if __name__ == '__main__':
    n1 = np.zeros((3, 4))
    n1 = np.ones((3, 4))
    # 单位方阵
    n1 = np.eye(3)
    # 单位矩阵
    n1 = np.eye(3, 4)
    # 少用
    n1 = np.empty((3, 4))
    n1 = np.full((3, 4), 8)
    # 创建序列  参数1表示起始值, 参数2表示结束值(不含)   参数3表示步长
    n1 = np.arange(10, 35, 3)
    # 等差数列
    n1 = np.linspace(0, 100, 5)
    # 指定起始值、终止值、样本数量和log底数
    n1 = np.logspace(0, 9, 10, 2)
    # 最小是10 ,最大是100(不含) ,10个数字
    n1 = np.random.randint(10, 100, 10)
    n1 = np.random.randint(10, 100, (3, 4))
    n1 = n1.reshape((2, 6))
    # reshape重塑方法,需要保证元素的数量不变,如果数量不一致,就会报错
    # n1 = n1.reshape((3, 6))
    print(n1)
