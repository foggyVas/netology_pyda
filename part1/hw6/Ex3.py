import re
"""
При помощи регулярных выражений напишите функцию, которая будет возвращать
акроним переданного в нее текста.

"""

current_text = input('Введите текст: ')
result = re.compile(r"(?:(?<=\s)|^)(?:[a-z]|\d+)", re.I)

print(''.join(result.findall(current_text.upper())))
