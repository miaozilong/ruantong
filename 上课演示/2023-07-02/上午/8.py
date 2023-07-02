# pycharm中 三种方式安装包      1. 写好代码后,光标放在包上,pycharm会提示安装,点击安装后,会自动安装
# 2. 使用控制台   不要直接输入cmd命令  按alt+F12 pip install scipy -i https://pypi.tuna.tsinghua.edu.cn/simple
#                                                             -i 表示使用镜像地址进行下载,会加快下载速度
# 3. 菜单 - settings - project - python interpreter 点击包名上的加号
from scipy import constants as C

if __name__ == '__main__':
    print("PI的值", C.pi)
    print("黄金比例", C.golden)
    print("光速", C.c)
