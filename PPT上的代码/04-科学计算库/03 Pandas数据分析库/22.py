import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('SalesReport.xlsx')
    # head = df.head()
    # print(head)
    groupby = df.groupby('产品')
    # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001EE66E285B0>
    print(groupby)
    # 获取"蒙古大草原绿色羊肉"组的所有数据
    group = groupby.get_group('蒙古大草原绿色羊肉')
    print(group)

    # 以产品分组,算"第 1 季度"的平均值
    mean = df.groupby('产品')['第 1 季度'].mean()
    print(mean)
