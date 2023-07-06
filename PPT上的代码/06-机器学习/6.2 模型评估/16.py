# 使用逻辑回归模型预测鸢尾花类别。鸢尾花数据集选取前70个样本，共两个类别，构造数据偏斜样本集
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
# 获取数据，并拼接数据使样本分布偏斜
iris = load_iris()
X = iris.data[0:70]
y = iris.target[0:70]
X = np.vstack((X[0:50],X[0:50],X))
y = np.hstack((y[0:50],y[0:50],y))
# 划分训练集和测试集
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=3)
lg = LogisticRegression(C=0.05)
lg.fit(X_train,y_train)
y_predict = lg.predict(X_test)
# 混淆矩阵
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_predict))
# 精准率和召回率
from sklearn.metrics import precision_score,recall_score
print(precision_score(y_test,y_predict))
print(recall_score(y_test,y_predict))
# 准确率
print(lg.score(X_test,y_test))