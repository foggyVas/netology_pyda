nameUser = input("Введите ваше имя: ")
m = str(input("Введите месяц рождения (пример: март): "))
d = int(input("Введите ваш день рождения (пример: 6): "))
m = m.upper()

# birthday = input()
# birthmonth = input()
if m == 'ЯНВАРЬ' and d >= 1 and d <= 20:
    zodiac = "Capricorn - Козерог"
if m == 'ЯНВАРЬ' and d >= 21 and d <= 31:
    zodiac = "Aquarius - Водолей"
if m == 'ФЕВРАЛЬ' and d >= 1 and d <= 19:
    zodiac = "Aquarius - Водолей"
if m == 'ФЕВРАЛЬ' and d >= 20 and d <= 31:
    zodiac = "Pisces - Рыба"
if m == 'МАРТ' and d >= 1 and d <= 20:
    zodiac = "Pisces - Рыба"
if m == 'МАРТ' and d >= 21 and d <= 31:
    zodiac = "Aries - Овен"
if m == 'АПРЕЛЬ' and d >= 1 and d <= 20:
    zodiac = "Aries - Овен"
if m == 'АПРЕЛЬ' and d >= 21 and d <= 31:
    zodiac = "Taurus - Телец"
if m == 'МАЙ' and d >= 1 and d <= 21:
    zodiac = "Taurus - Телец"
if m == 'МАЙ' and d >= 22 and d <= 31:
    zodiac = "Gemini - Близнецы"
if m == 'ИЮНЬ' and d >= 1 and d <= 21:
    zodiac = "Gemini - Близнецы"
if m == 'ИЮНЬ' and d >= 22 and d <= 31:
    zodiac = "Cancer - Рак"
if m == 'ИЮЛЬ' and d >= 1 and d <= 22:
    zodiac = "Cancer - Рак"
if m == 'ИЮЛЬ' and d >= 23 and d <= 31:
    zodiac = "Leo - Лев"
if m == 'АВГУСТ' and d >= 1 and d <= 23:
    zodiac = "Leo - Лев"
if m == 'АВГУСТ' and d >= 24 and d <= 31:
    zodiac = "Virgo - Дева"
if m == 'СЕНТЯБРЬ' and d >= 1 and d <= 23:
    zodiac = "Virgo - Дева"
if m == 'СЕНТЯБРЬ' and d >= 24 and d <= 31:
    zodiac = "Libra - Весы"
if m == 'ОКТЯБРЬ' and d >= 1 and d <= 23:
    zodiac = "Libra - Весы"
if m == 'ОКТЯБРЬ' and d >= 24 and d <= 31:
    zodiac = "Scorpio - Скорион"
if m == 'НОЯБРЬ' and d >= 1 and d <= 22:
    zodiac = "Scorpio - Скорион"
if m == 'НОЯБРЬ' and d >= 23 and d <= 31:
    zodiac = "Sagittarius - Стрелец"
if m == 'ДЕКАБРЬ' and d >= 1 and d <= 22:
    zodiac = "Sagittarius - Стрелец"
if m == 'ДЕКАБРЬ' and d >= 23 and d <= 31:
    zodiac = "Capricorn - Козерог"

print('{0}, your sings of zodiac: {1}'.format(nameUser, zodiac))
