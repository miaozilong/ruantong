import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import imageio

if __name__ == '__main__':
    face = misc.face()
    imageio.imwrite('face.jpg', face)
    plt.imshow(face)
    plt.show()
    # 输入/输出，显示图像
    # 基本操作 - 裁剪，翻转，旋转等
    # 图像过滤 - 去噪，锐化等
    # 图像分割 - 标记与不同对象相对应的像素
    flip_ud_face = np.flipud(face)
    plt.imshow(flip_ud_face)
    plt.show()