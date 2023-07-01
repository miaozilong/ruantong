import pandas as pd

if __name__ == '__main__':
    # 读取文件  参数1 文件的位置  可以是绝对或者相对路径   \表示转移
    # 附加,计算这行代码需要的时间
    df = pd.read_excel("./Online Retail.xlsx")
    # 清洗数据   找到需要的数据,移除不需要的数据
    # 清除带空值的行   how的值   any表示表示清除带空值的行, all表示所有是空值的情况下,再清除
    df.dropna(how='any')
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%Y-%m-%d')
    # 根据单价和数量,求价格
    df["Price"] = df['Quantity'] * df['UnitPrice']
    # 查看前几行数据 默认显示5行,可以指定行数
    # head = df.head(10)
    # print(head)
    #
    # 数据分析
    head10 = df[df['Quantity'] > 0].groupby('Country')['Quantity'].sum().sort_values(ascending=False).head(10)
    print(head10)

    # 求客单价  总价/总数量
    # 总价
    sum_all = df[df['Quantity'] > 0]['Price'].sum()
    # 总数量
    count = df[df['Quantity'] > 0]['InvoiceNo'].count()
    price_invoice = sum_all / count
    print("客单价是" + str(price_invoice))
    # 附加:用户消费行为分析 参考P41
