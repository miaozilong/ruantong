import numpy as np
import pandas as pd

if __name__ == '__main__':
    data1 = np.array([[84, 79, None], [75, 69, 88], [95, 83, 86], [88, 93, 76]])
    index1 = ['无情', '铁手', '追命', '冷血']
    column1 = ['语文', '数学', '英语']
    df = pd.DataFrame(data1, index1, column1)
    print(df)

    print(df.index)
    print(df.columns)
    print(df.dtypes)
    print(df.values)
    print(df.ndim)
    print(df.size)
    print(df.T)
    print(df.at['无情', '英语'])
    print(df.iat[0, 0])
    # 这里是左右都闭
    print(df.loc['无情':'追命', '数学':'英语'])
    # 这里是左闭右开
    print(df.iloc[0:1, 0:2])
    print(df.info())
    print(df.describe())
    print(df.head(2))
    print(df.tail(2))
    print(df.isnull())
    # 数据为None的显示未True
    print(df.notnull())
    print()
