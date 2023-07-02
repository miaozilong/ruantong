import numpy as np
import pandas as pd

if __name__ == '__main__':
    # 生成DataFrame数据
    # 1. 使用ndarray
    data1 = np.array([[84, 79, 82], [75, 69, 88], [95, 83, 86], [88, 93, 76]])
    names1 = ['无情', '铁手', '追命', '冷血']
    columns1 = ['语文', '数学', '英语']
    df1 = pd.DataFrame(data=data1, index=names1, columns=columns1)
    print(df1)
    # 2. 使用list
    # 附加题:略
    # 3 使用字典进行创建
    data3 = {
        '吕布': [100, 43, 40, 20],
        '关羽': [98, 82, 79, 60],
        '赵云': [99, 87, 89, 99],
        '马超': [97, 85, 62, 55]
    }
    index3 = ['武力值', '统率', '智力', '人格']
    df3 = pd.DataFrame(data=data3, index=index3)
    print(df3)
    # 附加题:使用Series进行创建

