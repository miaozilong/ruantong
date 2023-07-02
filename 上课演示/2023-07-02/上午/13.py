import numpy as np
import pandas as pd

if __name__ == '__main__':
    data1 = np.array([[84, 79, None], [75, 69, 88], [95, 83, 86], [88, 93, 76]])
    names1 = ['无情', '铁手', '追命', '冷血']
    columns1 = ['语文', '数学', '英语']
    df1 = pd.DataFrame(data=data1, index=names1, columns=columns1)
    print(df1.index)
    print(df1.columns)
    print(df1.values)
    print(df1.ndim)
    print(df1.shape)
    print(df1.size)
    print(df1.T)
    print(df1.at['铁手', '英语'])
    print(df1.info())
    print('------------')
    print(df1.describe())
    print(df1.tail(2))
    print(df1.isnull())
    print(df1.notnull())
