import numpy as np
from sklearn.model_selection import train_test_split
X, y = np.arange(10).reshape((5, 2)), range(5)
print(X)
print(list(y))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
print('训练集：')
print(X_train)
print(y_train)
print('测试集：')
print(X_test)
print(y_test)
print()