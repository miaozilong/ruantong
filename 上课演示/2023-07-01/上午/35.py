import numpy as np
import pandas as pd

if __name__ == '__main__':
    # 比较耗时
    df = pd.read_excel('Online Retail.xlsx', )
    # 统计数据前,需要数据清洗
    # 只要有空值的行,都进行清理
    df.dropna(how='any')
    # 对日期进行转换
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%Y-%m-%d')
    df['Price'] = df['Quantity'] * df['UnitPrice']
    # head函数默认显示前5条数据
    head = df.head()
    print(head)
    head10 = df[df['Quantity'] > 0].groupby('Country')['Quantity'].sum().sort_values(ascending=False).head(10)
    print(head10)

    # 附加: 求客单价   进行用户消费行为分析
