import os
from py_scripts import functions as fun


conn, cursor = fun.connect_to_db(os.getenv('PASSWORD'))

#создание таблицы

try:
    cursor.execute("""CREATE TABLE tourism_data (
                    TERRITORY_CODE varchar(30),
                    TERRITORY_NAME varchar(50),
                    DATE_OF_ARRIVAL date,
                    TRIP_TYPE varchar(30),
                    VISIT_TYPE varchar(30),
                    HOME_COUNTRY varchar(50),
                    HOME_REGION varchar(100),
                    HOME_CITY varchar(100),
                    GOAL varchar(100),
                    GENDER varchar(10),
                    AGE varchar(30),
                    INCOME varchar(50),
                    DAYS_CNT int,
                    VISITORS_CNT int,
                    SPENT numeric(30,20));
              """)
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print("Error: %s" % error)
    conn.rollback()
print('Table created')

# Закрываем соединение

cursor.close()
conn.close()
