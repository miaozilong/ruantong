import numpy as np
import pandas as pd

if __name__ == '__main__':
    data = np.linspace(5, 20, 5)
    # data 表示数据   index表示索引或者标签
    series = pd.Series(data, index=[0, 1, 2, 3, 4])
    print(series)
    #  指定标签名
    series = pd.Series(data, index=['标签1', '标签2', '标签3', '标签4', '标签5'])
    print(series)

    # 使用ndarray创建dataframe
    data1 = np.array([[84, 79, 92], [75, 69, 88], [95, 83, 86], [88, 93, 76]])
    index1 = ['无情', '铁手', '追命', '冷血']
    columns1 = ['语文', '数学', '英语']
    # index代表索引   columns代表列名
    df1 = pd.DataFrame(data=data1, index=index1, columns=columns1)
    print(df1)
    # 附加题:data使用list进行创建
    # 使用字典进行创建
    data3 = {'吕布': [100, 43, 40, 20], '关羽': [98, 82, 79, 60], '赵云': [99, 87, 89, 99], '马超': [97, 85, 62, 55]}
    index3 = ['武力值', '统率', '智力', '人格']
    df3 = pd.DataFrame(data3, index=index3)
    print(df3)
    # 附加题:使用Series进行创建  可以使用zip函数组合多个Series
