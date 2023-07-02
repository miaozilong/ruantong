import imageio
import numpy as np
from scipy import ndimage
from scipy import misc
from scipy import datasets
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 自动取github上下载数据
    face = datasets.face()
    imageio.imwrite('face.jpg', face)
    plt.imshow(face)
    plt.show()
    #     对图像进行处理
    flipud = np.flipud(face)
    plt.imshow(flipud)
    plt.show()