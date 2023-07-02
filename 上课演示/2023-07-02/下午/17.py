import pandas as pd
if __name__ == '__main__':
    df = pd.read_table("SalesReport.txt")
    print(df)
    df = pd.read_csv("SalesReport.csv")
    print(df)
    df = pd.read_excel("SalesReport.xlsx")
    print(df)
    df = pd.read_json("users.json")
    print(df)
    # read_html读取到的是列表
    # df = pd.read_html("https://www.fooish.com/html/table.html")[0]
    # 无法演示,需要连接数据库
    # pd.read_sql()

    df = pd.read_excel("SalesReport.xlsx")
    print(df)
    # df = df.drop(columns=['客户'], index=[0])
    df = df.drop_duplicates()
    print(df)
    # 删除空值  how='any' 表示任一列是空,则删除   how='all' 表示所有列都是空时,再删除
    df = df.dropna(how='all')
    print(df)

    # 填充空值
    df = df.fillna({'客户': '内部购买', '第 1 季度': 0})
    print(df)

    # like 表示根据索引号进行筛选  regex 表示根据正则进行筛选
    df = df.filter(like='8', axis=0)
    print(df)
    df = df.replace('蒙古大草原绿色羊肉', '新疆大草原绿色羊肉')
    print(df)
    df.to_excel('a.xlsx')
