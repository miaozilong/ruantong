import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('general_sg.xlsx')
    duplicated = df.duplicated()
    print(duplicated)
    df = df.drop_duplicates()
    ts = df.iloc[:, 1]
    ts_mean = ts.mean()
    zl = df.iloc[:, 3]
    zl_mean = zl.mean()
    zz = df.iloc[:, 4]
    zz_mean = zz.mean()
    df['统率'] = df['统率'].fillna(ts_mean)
    df['智力'] = df['智力'].fillna(zl_mean)
    df['政治'] = df['政治'].fillna(zz_mean)
    print(df)
    print(df.describe())
    # df = df.sort_values(by='武力', ascending=False).head(3)
    print(df)
    df['综合得分'] = df['统率'] * 0.3 + df['智力'] * 0.30 + df['武力'] * 0.15 + df['政治'] * 0.25
    df = df.sort_values(by='综合得分', ascending=False).head(3)
    print(df)
