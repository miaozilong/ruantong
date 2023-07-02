import pandas as pd

if __name__ == '__main__':
    # 使用字典进行创建
    data3 = {'吕布': [100, 43, 40, None], '关羽': [98, 82, 79, 60], '赵云': [99, 87, 89, 99], '马超': [97, 85, 62, 55]}
    index3 = ['武力值', '统率', '智力', '人格']
    df3 = pd.DataFrame(data3, index=index3)
    # 标签
    print(df3.index)
    print(df3.columns)
    print(df3.dtypes)
    print(df3.values)
    print(df3.ndim)
    print(df3.shape)
    print(df3.size)
    print(df3.T)
    print(df3.at['武力值', '马超'])
    print(df3.iat[0, 3])
    print(df3.loc['统率':'人格', '赵云':'马超'])
    # 自行测试iloc
    print(df3.info())
    print(df3.describe())
    print(df3.tail(2))
    print(df3.isnull())
