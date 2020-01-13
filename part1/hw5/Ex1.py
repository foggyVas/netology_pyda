import json
"""
Переведите содержимое файла purchase_log.txt в словарь purchases вида:

{'1840e0b9d4': 'Продукты', ...}
"""


number_of_lines = int(input('Введите кол-во строк для просмотра: '))

with open('purchase_log.txt', 'r', encoding="UTF-8") as f:

    for i in range(number_of_lines):
        step = json.loads(f.readline())
        purchases = {step['user_id']: step['category']}
        print(purchases)
