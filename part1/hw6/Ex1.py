import re

vehicle_reg_plates_list = ['а798ар177', 'Т552ес35', 'о225КО161', 'а552kе139'
                           'з234ап99']



def validate_vehicle_reg_plates(text):
    """Выводит отдельно номер и регион, если транспортный номер корректный"""
    look_for = r'([а-я])(\d{3})([а-я]{2})(\d+)'
    try:
        number = re.match(look_for, text.lower()).group(2)
        region = re.match(look_for, text.lower()).group(4)
        return number, region
    except:
        return print('Введите не корректный транспортный номер')


print(validate_vehicle_reg_plates('а234ап99'))
