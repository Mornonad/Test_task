import os
import psycopg2
import psycopg2.extras as extras
import shutil
import sys
import warnings
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

warnings.filterwarnings('ignore')
env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)


def connect_to_db(password):
    '''Создание подключения к PostgreSQL базе'''
    try:
      conn = psycopg2.connect(f"""
                              host=rc1a-12rz9s6o3ihxc90v.mdb.yandexcloud.net
                              port=6432
                              dbname=tourism
                              user=user1
                              password={password}
                              target_session_attrs=read-write
                          """)

      # Отключение автокоммита
      conn.autocommit = False

      # Создание курсора
      cursor = conn.cursor()

    except (Exception, psycopg2.DatabaseError) as error:
      print(error)

    print(f"Connection to the database successful")
    return conn, cursor


def execute_values(cursor, conn, df, table):
    '''функция для вставки данных в базу данных'''

    # создание списка tupples из значений датафрейма
    tuples = [tuple(x) for x in df.to_numpy()]

    # Comma-separated dataframe columns
    cols = ','.join(list(df.columns))

    # SQL запрос
    query  = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)

    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        return 1
    print(f'Data has been inserted to {table}')


def move_file(file_name):
  '''функция для переноса обработанных файлов в архив'''
  try:
    shutil.move(
              f'{os.getenv("FILES_PATH_PREFIX")}\\{file_name}',
              f'{os.getenv("PROCESSED_FILES_DIR")}\\{file_name}.backup'
          )
  except OSError as err:
    print(err)
  print(f'Processed file {file_name} has been moved to archive')