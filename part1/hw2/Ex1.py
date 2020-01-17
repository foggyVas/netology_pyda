geo_logs = [['visit1', ['Москва', 'Россия']],
            ['visit2', ['Дели', 'Индия']],
            ['visit3', ['Владимир', 'Россия']],
            ['visit4', ['Лиссабон', 'Португалия']],
            ['visit5', ['Париж', 'Франция']],
            ['visit6', ['Лиссабон', 'Португалия']],
            ['visit7', ['Тула', 'Россия']],
            ['visit8', ['Тула', 'Россия']],
            ['visit9', ['Курск', 'Россия']],
            ['visit10', ['Архангельск', 'Россия']]
            ]

geo_logs_rus = list()

for i in range(len(geo_logs)):
    if 'Россия' in geo_logs[i][1]:
        geo_logs_rus.append(geo_logs[i])


print(geo_logs_rus)
