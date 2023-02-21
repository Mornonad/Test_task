import json
import pandas as pd
from datetime import datetime

#загрузка дынных из файла в dataframe

with open('final.csv', encoding='utf-8', mode='r') as f:
    df = pd.read_csv(f, sep=',', header=0, parse_dates=['DATE_OF_ARRIVAL'],low_memory=False)

#Замена типов (только тех, которые используются в вычислениях)

df.drop(df.loc[df.TERRITORY_CODE != '22701000'].index, inplace=True)
df[['DAYS_CNT', 'VISITORS_CNT']] = df[['DAYS_CNT', 'VISITORS_CNT']].apply(pd.to_numeric, errors='coerce').astype(pd.Int64Dtype())
df['DATE_OF_ARRIVAL'] = pd.to_datetime(df['DATE_OF_ARRIVAL'], format="%Y-%m-%d", errors='coerce')
df['SPENT'] = pd.to_numeric(df['SPENT'], errors='coerce')
df = df.replace({pd.NA: None})
df.columns = map(str.lower, df.columns)

key_list = ['trip_type', 'visit_type', 'home_region', 'goal', 'gender', 'age', 'income']

my_dict = {key: [] for key in key_list}

for key in key_list:
    names = df[key].value_counts(dropna=False).keys().tolist()
    counts = df[key].value_counts(dropna=False).tolist()

    for name, count in zip(names, counts):
        my_dict[key].append({"name": name, "count": count})

result = {"parametres": my_dict}

with open("result.json", "w", encoding="utf8") as f:
      json.dump(result, f, ensure_ascii=False, indent=2)

