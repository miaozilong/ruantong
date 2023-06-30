from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy_demo as np
import pymysql

if __name__ == '__main__':
    # budget
    # original_language_id
    # release_date
    # runtime

    # revenue              bigint,
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='data'
    )

    query = pd.read_sql_query("""
               select budget,  runtime
                from movie
                where budget > 0
                and runtime > 0
                and revenue >0 
                order by id 
                """, conn)
    df_features = pd.DataFrame(query, columns=['budget', 'runtime'])
    query = pd.read_sql_query("""
               select revenue
                from movie
                where budget > 0
                and runtime > 0
                and revenue >0 
                order by id
                """, conn)
    df_target = pd.DataFrame(query, columns=['revenue'])

    X_train, X_test, y_train, y_test = train_test_split(df_features, df_target, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    predict = model.predict(X_test)
    print(predict)
    print(y_test)
    print()