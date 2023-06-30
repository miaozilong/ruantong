import numpy as np
import pandas as pd
from loguru import logger as log

log.add('file_{time:YYYY-MM-DD}.log', format="{name} {level} {message}", level="TRACE", rotation='5 MB',
        encoding='utf-8')
if __name__ == '__main__':
    log.debug("开始")
    df = pd.read_excel("Online Retail.xlsx")
    log.debug("结束")
    # 删除缺失CustomID对应数据内容
    df = df.dropna(how='any')
    # 修改InvoiceDate格式，只取年月作为日期内容
    # 12/1/2010 8:26转换为2010-12-01
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format="%Y-%m-%d %H:%M:%S")
    df['Price'] = df['Quantity'] * df['UnitPrice']
    head = df.head()
    print(head)
    print(df.info())
    # 获取产品数量大于0，按国家分组，对销售金额进行求和，从大到小进行排序
    head10 = df[df['Quantity'] > 0].groupby('Country')['Quantity'].sum().sort_values(ascending=False).head(10)
    print(head10)
    # 客单价多少？
    sumPrice = df[df['Quantity'] > 0]['Price'].sum()
    countID = df[df['Quantity'] > 0]['InvoiceNo'].count()
    avgPrice = sumPrice / countID
    print("平均客单价：", avgPrice)
    # 用户消费行为分析
    describe = df[df['Quantity'] > 0].groupby('CustomerID').agg(
        {'InvoiceNo': 'nunique', 'Quantity': 'sum', 'Price': 'sum'}).describe()
    print(describe)
    print()
