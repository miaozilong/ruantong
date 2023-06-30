# Press the green button in the gutter to run the script.

import pandas as pd
import pymysql

if __name__ == '__main__':
    df = pd.read_csv('D:/移动云盘同步文件夹/18801283695/工作资料/软通动力/tmdb电影数据/tmdb_5000_movies.csv',
                     encoding='utf-8')
    df = df.where(df.notnull(), None)
    df['runtime'] = df['runtime'].fillna(0.0)
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='data'
    )
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    cursor.execute('truncate table movie')
    for row in df.itertuples():
        id = getattr(row, 'id')
        budget = getattr(row, 'budget')
        homepage = getattr(row, 'homepage')
        original_language_id = getattr(row, 'original_language')
        original_title = getattr(row, 'original_title')
        overview = getattr(row, 'overview')
        release_date = getattr(row, 'release_date')
        revenue = getattr(row, 'revenue')
        runtime = getattr(row, 'runtime')
        title = getattr(row, 'title')
        try:
            # 执行sql语句
            args = (
                id, budget, homepage, original_language_id, original_title, overview, release_date, revenue, runtime,
                title)
            cursor.execute("""
            insert into movie 
            (id, budget, homepage, original_language_id, original_title, overview, release_date, revenue, runtime, title)
            values
             (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, args)
            # 提交到数据库执行
            conn.commit()
        except Exception as e:
            print(e)
            # Rollback in case there is any error
            conn.rollback()
    # 关闭数据库连接
    cursor.close()
    conn.close()
