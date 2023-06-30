import numpy as np
import pandas as pd

if __name__ == '__main__':
    data1 = np.array([[84, 79, 92], [75, 69, 88], [95, 83, 86], [88, 93, 76]])
    index1 = ['无情', '铁手', '追命', '冷血']
    column1 = ['语文', '数学', '英语']
    df1 = pd.DataFrame(data1, index1, column1)
    print(df1)
    # 通过1ist创建
    data2 = [[95, 65, 75], [70, 95, 88], [80, 90, 86], [90, 93, 80]]
    index2 = ['郭靖', '黄蓉', '杨康', '杨过']
    columns2 = ['武力值', '智商', '情商']
    df2 = pd.DataFrame(data2, index2, columns2)
    # 通过dict创建
    data3 = {'吕布': [100, 43, 40, 20], '关羽': [98, 82, 79, 60], '赵云': [99, 87, 89, 99], '马超': [97, 85, 62, 55]}
    index3 = [' 武力值', '统率', '智力', '人格']
    df3 = pd.DataFrame(data3, index=index3)
    # 通过Series创建
    arr = np.array([99, 87, 89, 99])
    s1 = pd.Series(arr)
    s2 = pd.Series([100, 43, 40, 20])
    df4 = pd.DataFrame(zip(s1, s2), index=['武力值', '统率', '智力', '人格'], columns=['赵云', '吕布'])
    print()