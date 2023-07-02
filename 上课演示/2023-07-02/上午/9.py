import numpy as np
import pandas as pd

if __name__ == '__main__':
    # 等差数列
    arr = np.linspace(10, 20, 5)
    print(arr)
    index = np.array([1, 2, 3, 4, 5])
    # 生成Series  data为Series中的数据    index为Series中的索引
    series = pd.Series(data=arr, index=index)
    print(series)
    # 标签不要重复
    series = pd.Series(data=arr, index=['标签1', '标签2', '标签3', '标签4', '标签5'])
    print(series)
