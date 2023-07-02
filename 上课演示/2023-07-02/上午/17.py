import pandas as pd

if __name__ == '__main__':
    # 参数1,文件路径
    df = pd.read_table("SalesReport.txt", encoding='UTF-8')
    print(df)
    df = pd.read_csv("SalesReport.csv", encoding='UTF-8')
    print(df)

    df = pd.read_excel("SalesReport.xlsx")
    print(df)

    df = pd.read_json("users.json")
    print(df)

    # read_html读取页面上所有的表格
    # df = pd.read_html('https://www.fooish.com/html/table.html')[0]
    # print(df)

    # read_sql()   需要连接数据库,再进行读取

    df = pd.read_excel("SalesReport.xlsx")
    df = df.drop(columns=['客户'])
    print(df)

    # subset 表示根据哪一列判断是否有重复值  默认表示所有
    # keep 表示重复值保留哪一个  first表示第一个  last最后一个  默认为first
    # inplace 是否替换原有DataFrame对象  默认不替换
    df = df.drop_duplicates(subset=['产品'], keep='last')
    print(df)

    # 清除空值的行   how='any' 表示任一单元格为空  就删除    how = all   表示所有单元格为空 再删除
    df = df.dropna(how='any')
    df = pd.read_excel("SalesReport.xlsx")
    df = df.duplicated()
    print(df)
    df = pd.read_excel("SalesReport.xlsx")
    df = df.fillna({'客户': '内部客户', "第 1 季度": 0})
    print(df)
    df = df.filter(like='8', axis=0)
    df = df.replace("蒙古大草原绿色羊肉", "蒙古大草原绿色牛肉")
    print(df)
