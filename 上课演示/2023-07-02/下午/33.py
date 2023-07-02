import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('general_sg.xlsx')
    # 去重
    df = df.drop_duplicates()
    print(df)

    # 求平均分
    ts = df.iloc[:, 1]
    zl = df.iloc[:, 3]
    zz = df.iloc[:, 4]
    df['统率'] = df['统率'].fillna(ts.mean())
    df['智力'] = df['智力'].fillna(zl.mean())
    df['政治'] = df['政治'].fillna(zz.mean())
    print(df)
    print(df.describe())

    # 按照武力进行排行
    # df = df.sort_values(by='武力', ascending=False).head(3)
    # print(df)

    df['综合评分'] = df['统率'] * 0.3 + df['智力'] * 0.3 + df['武力'] * 0.15 + df['政治'] * 0.25

    df = df.sort_values(by='综合评分', ascending=False).head()
    print(df)
    df.to_excel('g-score.xlsx')
