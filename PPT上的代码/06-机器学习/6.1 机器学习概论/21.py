import numpy as np
import pandas as pd
from sklearn import datasets

# 生成一个相似的二元分类数据集，有10个维度
hastie_10_2 = datasets.make_hastie_10_2()
print(hastie_10_2)
# 生成一个多类单标签数据集，为每个类分配一个或多个正太分布的点集
blobs = datasets.make_blobs()
print(blobs)
