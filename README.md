# ETL проект

Глава города Нижнего Новгорода поручил подготовить аналитический дашборд по состоянию туризма в городе. 
Все необходимые данные собирает третья сторона, которая автоматизировано делится CSV выгрузками. 

Задача – настроить автоматическую обработку и загрузку данных, поступающих от третей стороны, и, на основе полученной информации подготовить аналитику, которая позволит Главе города принимать управленческие решения.

## Основные этапы

  1. Создать базу данных PostgreSQL на Yandex.Cloud.
  2. С помощью Python скрипта предобработать тестовую выгрузку и загрузить ее в БД. 
  3. С помощью Yandex.DataLens и БД подготовить дашборд по полученным данным. 
  4. Основные ключевые показатели собрать в JSON файл и настроить локальный RestAPI с использованием Flask, для получения этого файла с помощью GET/POST запроса.

## Результат разработки

  1. Таблица в БД создается с помощью create_tables.py.

  2. CSV выгрузка загружается в ту же папку, где находится основная программа - main.py.
  3. Для автоматического запуска по расписанию, можно использовать Cron.
  4. Подготовленный дашборд можно найти по [ссылке](https://datalens.yandex.ru/12xjxqvxv0yir-sostoyanie-turizma-v-g-nizhniy-novgorod-na-1-polugodie)

  Дашборд состоит из 3х разделов:
  
  - Общая статистика;
  - Информация о туристах;
  - Информация о расходах туристов во время поездки в Нижний Новгород.
  
  На основе этих данных можно сделать выводы о том, в какие месяцы больше поток туристов, какой возрас большинства туристов, каков их доход и тд.
  
<img src="https://github.com/Mornonad/Test_task/blob/main/resourses/1.PNG" alt= “[Дэшборд1” width="50%" height="50%">
<img src="https://github.com/Mornonad/Test_task/blob/main/resourses/2.PNG" alt= “[Дэшборд2” width="50%" height="50%">
<img src="https://github.com/Mornonad/Test_task/blob/main/resourses/3.PNG" alt= “[Дэшборд3” width="50%" height="50%">

