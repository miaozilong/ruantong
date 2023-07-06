import numpy as np
import pandas as pd
from sklearn import datasets

# 下载在线的大型数据集
faces = datasets.fetch_olivetti_faces(data_home=None,
                                      shuffle=False,
                                      random_state=0,
                                      download_if_missing=True)
print(faces.keys())
