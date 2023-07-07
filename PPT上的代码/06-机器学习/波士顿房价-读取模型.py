from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import joblib

if __name__ == '__main__':
    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
    # 1. 加载数据
    # 2. 获取特征和目标
    # 3. 获取训练和测试
    # 4. 选择模型
    # 5. 预测
    # 6. 比较结果
    features = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]
    print()

    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)
    print()
    model = joblib.load('lr.model')
    model.fit(X_train, y_train)
    print(model.predict(X_test))
    print(y_test)
