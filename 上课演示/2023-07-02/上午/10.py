import imageio
from scipy import datasets
import matplotlib.pyplot as plt
if __name__ == '__main__':
    # 获取脸的数据    会在gtihub获取人脸的最新数据   自行处理网络问题
    face = datasets.face()
    # 参数1  文件路径       参数2  图像的数据
    imageio.imwrite("face.jpg", face)
    #  显示图像
    plt.imshow(face)
    plt.show()

