import numpy as np
import pandas as pd

if __name__ == '__main__':
    # df = pd.read_table('SalesReport.txt')
    # head = df.head()
    # print(head)

    # df = pd.read_csv('SalesReport.csv')
    # head = df.head()
    # print(head)

    # df = pd.read_excel('SalesReport.xlsx')
    # head = df.head()
    # print(head)

    # df = pd.read_json('users.json')
    # head = df.head()
    # print(head)

    # df = pd.read_html('https://www.fooish.com/html/table.html')[0]
    # head = df.head()
    # print(head)

    # read_sql 需要连接数据库

    df = pd.read_excel('SalesReport.xlsx')
    #
    # df = df.drop(columns=['客户'], index=[0])

    # subset = None 用于指定重复的列 默认表示所有  subset=['产品']
    # keep='first' | 'last'
    # inplace : boolean, default False是直接在原来数据上修改还是保留一个副本 默认保留副本
    # df = df.drop_duplicates(subset=['产品'], keep='first', inplace=False)
    # df = df.dropna(how='any')

    # 判断每一行数据是否重复
    # df = df.duplicated()
    # 填充为同一个值
    # df = df.fillna('数据为空')
    # 使用字典填充
    # df = df.fillna({'客户': '内部客户', '第 1 季度': '没有销量'})

    # df = df.filter(items=['产品', '客户'])
    # 索引中带0的
    # df = df.filter(like='8', axis=0)

    df = df.replace("蒙古大草原绿色羊肉","蒙古大草原绿色牛肉")

    head = df.head()
    print(head)
