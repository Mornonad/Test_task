import numpy as np
import os
import pandas as pd
from py_scripts import functions as fun

# загрузка данных из файла в dataframe

with open(f'{os.getenv("FILES_PATH_PREFIX")}\\final.csv', encoding='utf-8', mode='r') as f:
    df = pd.read_csv(f, sep=',', header=0, parse_dates=['DATE_OF_ARRIVAL'],low_memory=False)

# Удаление некорректных данных и замена типа данных

df.drop(df.loc[df.TERRITORY_CODE != '22701000'].index, inplace=True)
df[['DAYS_CNT', 'VISITORS_CNT']] = df[['DAYS_CNT', 'VISITORS_CNT']].apply(pd.to_numeric, errors='coerce').astype(pd.Int64Dtype())
df['DATE_OF_ARRIVAL'] = pd.to_datetime(df['DATE_OF_ARRIVAL'], format="%Y-%m-%d", errors='coerce')
df['SPENT'] = pd.to_numeric(df['SPENT'], errors='coerce')
df = df.replace({pd.NA: None})

# подключение к серверу

conn, cursor = fun.connect_to_db(os.getenv('PASSWORD'))

# загрузка данных на сервер

fun.execute_values(cursor, conn, df, 'tourism_data')

# Закрываем соединение

cursor.close()
conn.close()

# перемещаем обработанный файл

fun.move_file('final.csv')

