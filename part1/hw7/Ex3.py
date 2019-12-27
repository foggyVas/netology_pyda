from datetime import datetime
"""
Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:


Напишите функцию, которая проверяет эти даты на корректность. Т. е. для каждой
даты возвращает True (дата корректна) или False (некорректная дата).
"""

stream = ['2018-02-29', '2018-04-02', '2018-19-02', '2018-04-02']

def is_date_correct(stream):

    for date in stream:
        try:
            datetime.strptime(date, '%Y-%m-%d')
            print(f"{date} - True - (дата корректна)")
        except:
            print(f"{date} - False - (некорректная дата)")

is_date_correct(stream)
