"""
В примере поиска с помощью кортежей мы использовали 3 столбца.
Напишите функцию, которая формирует словарь для поиска по n столбцам.
"""
random_line = [31, 15800, 4, 68171, 24, 3922, 2, 79332]

n = int(input("Для поиска нужного эл-та введите значение n <= 7: "))

random_line = random_line[:n]


stats_list = []

with open('random.csv') as f:
    for line in f:
        line = line.strip().split(',')
        stats_list.append(line)


line_to_find = [str(i) for i in random_line]

for line in stats_list:
    if line[:n] == line_to_find:
        print(line[n])
        break
        
