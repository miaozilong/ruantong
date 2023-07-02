import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('general_sg.xlsx')
    duplicated = df.duplicated()
    print(duplicated)
    df = df.drop_duplicates()
    # print(df)

    # 对缺失值进行填充
    ts = df.iloc[:, 1]
    wl = df.iloc[:, 1]
    zl = df.iloc[:, 1]
    zz = df.iloc[:, 1]
    df['统率'] = df['统率'].fillna(ts.mean())
    df['武力'] = df['武力'].fillna(ts.mean())
    df['智力'] = df['智力'].fillna(ts.mean())
    df['政治'] = df['政治'].fillna(ts.mean())
    print(df)
    print(df.describe())

    wlhead = df.sort_values(by='武力', ascending=False).head()
    print(wlhead)

    df['综合得分'] = df['统率'] * 0.3 + df['智力'] * 0.3 + df['武力'] * 0.15 + df['政治'] * 0.25
    print(df)
    df.to_excel('a.xlsx')
