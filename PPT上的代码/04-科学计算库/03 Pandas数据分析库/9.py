import numpy as np
import pandas as pd

if __name__ == '__main__':
    arr = np.array(['张三', 18, '男', 65.0, '团员'])
    print(arr)
    index1 = np.array([1, 2, 3, 4, 5])
    # 不指定索引，默认从0开始
    s11 = pd.Series(arr)
    print(s11)
    # 通过index指定索引
    s12 = pd.Series(arr, index=index1)
    print(s12)

    # 手动设置标签
    s13 = pd.Series(arr, index=['姓名', '年龄', '性别', '体重', '政治面貌'])
    print(s13)
