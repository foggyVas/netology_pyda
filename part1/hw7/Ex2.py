from datetime import datetime, timedelta
""""
Дополните функцию из первого задания проверкой на корректность дат.
В случае неверного формата или если start_date > end_date должен возвращаться
пустой список.
"""


def date_range(start_date, end_date):
    try:
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')

        return [datetime.strftime(start_date_dt + timedelta(days=days_difference), '%Y-%m-%d')
                for days_difference in range((end_date_dt - start_date_dt).days)]#, (end_date_dt - start_date_dt).days
    except:
        return []

print(date_range('2019-12-24', '2019-12-31'))
