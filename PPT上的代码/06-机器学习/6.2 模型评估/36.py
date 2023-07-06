# 加载鸢尾花数据集，根据其特征将其聚成三类，将聚类结果标签与原数据标签对比，评估聚类模型质量
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
# 加载兰德指数和互信息评估函数
from sklearn.metrics import adjusted_rand_score,adjusted_mutual_info_score
iris = load_iris()
X = iris.data
y = iris.target
# 聚类问题数据需标准化
X_scaled = MinMaxScaler().fit_transform(X)
kmeans = KMeans(n_clusters=3,random_state=321)
kmeans.fit(X_scaled)
# 获取聚类标签
y_km = kmeans.labels_
print(adjusted_rand_score(y,y_km))
print(adjusted_mutual_info_score(y,y_km))
