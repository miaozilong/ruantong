import numpy as np
import pandas as pd

if __name__ == '__main__':
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], index=['张三', '李四'], columns=['语文', '数学', '英语'])
    df.to_csv('a.csv')
    df.to_excel('a.xlsx')
    # 默认force_ascii为True  需要指定为false 否则会有乱码
    df.to_json('a.json', force_ascii=False)
    df.to_html('a.html')
    # 需要数据库连接
    # df.to_sql('a.sql')
