income = int(input("Введите заработанную плату в месяц: "))
mortgagePercent = int(input("Введите сколько процентов уходит на ипотеку: "))
livingStandartPercent = int(input("Введите сколько процентов уходит на жизнь: "))
bonus = int(input("Введите количество премий за год: "))
livingStandart = int((income * livingStandartPercent / 100) * 12)
mortgage = int((income * mortgagePercent / 100) * 12)
accumulation = int((income * (12 + bonus) - mortgage - livingStandart))

print('За год на ипотеку было потрачено: {0} '
      '\nЗа год было накоплено: {1}'.format(
    mortgage, accumulation))
    
