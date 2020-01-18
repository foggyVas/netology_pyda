import pandas as pd

"""
Для датафрейма log из материалов занятия создайте столбец source_type по следующим
правилам:

если источник traffic_source равен yandex или google, то в source_type ставится organic
для источников paid и email из России - ставим ad
для источников paid и email не из России - ставим other
все остальные варианты берем из traffic_source без изменений
"""

log = pd.read_csv('visit_log.csv', sep=';')

log.loc[
    (log['traffic_source'].isin(['yandex','google'])), 'source_type'
] = 'organic'

log.loc[
    (log['traffic_source'].isin(['paid','email'])) &
    (log.region == 'Russia'), 'source_type'
] = 'other'

log.loc[
    (log['traffic_source'].isin(['paid','email'])) &
    (log.region != 'Russia'), 'source_type'
] = 'ad'

groups_source = log.groupby('traffic_source')
print(groups_source.groups.keys())

log.loc[
    (log['traffic_source'].isin(['direct'])), 'source_type'
] = 'direct'

print(log)
