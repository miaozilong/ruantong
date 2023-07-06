import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.model_selection import cross_val_score, train_test_split
if __name__ == '__main__':
    iris = load_iris()
    X_train,X_test,y_train,y_test = train_test_split(iris.data, iris.target,test_size=0.3,random_state=31)
    # 使用for循环进行网格搜索和交叉验证
    for c in [0.001, 0.01, 0.1, 1, 10, 100]:
        lg = LogisticRegression(C=c)
        scores = cross_val_score(lg, X_train, y_train, cv=5)   #在训练集和验证集上进行交叉验证
        score = np.mean(scores)
        print({'c':c,'score':score})
    # LogisticRegressionCV整合了交叉验证
    c=[0.001, 0.01, 0.1, 1, 10, 100]
    lg = LogisticRegressionCV(Cs=c,cv=5)
    lg.fit(X_train,y_train)
    score = lg.score(X_train,y_train)
    c = lg.C_
    print({'c':c,'score':score})
