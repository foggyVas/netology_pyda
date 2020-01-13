documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def p_what_number():
    input_number = input('Введите номер документа: ')
    for document in documents:
        if document['number'] == input_number:
            print(document['name'])

def s_what_number():
    input_number = input('Введите номер документа: ')
    for shelf, cell in directories.items():
        if input_number in cell:
            print('Номер полки: ', shelf)

def l_all_docs():
    for document in documents:
        print('{} {} {}'.format(document['name'], document['type'],
                                document['number']))

def as_add_shelf():
    input_number = input('Введите номер полки: ')
    if input_number in directories.keys():
        print('Эта полка уже существует')
    else:
        print('Полка номер: ', input_number, 'добавлена')
        directories[input_number] = []

def add_person():
    print('Человек добавлен, но это не точно')

def del_person():
    print('Человек удален, но это не точно')

def move_person():
    print('Человек перемещен, но это не точно')

def user_commands():
    print('Вы моожете узнать следующую информацию \n 1. ФИО человека \n '
          '2. № Полки где хранится документ\n 3. Вывести список всех людей'
          '\n 4. Добавить новую полку \n 5. Добавить документ \n 6. Передвинуть'
          ' документы человека на другую полку \n 7. Удалить документ')
    user_input = input('Выберите пункт из меню: ')
    if user_input == '1':
        p_what_number()
    elif user_input == '2':
        s_what_number()
    elif user_input == '3':
        l_all_docs()
    elif user_input == '4':
        as_add_shelf()
    elif user_input == '5':
        print('В разработке')
        # add_person()
    elif user_input == '6':
        print('В разработке')
        #  move_person()
    elif user_input == '7':
        print('В разработке')
        #  del_person()
    else:
        print('Введен не корректный номер, попробуйте снова')


user_commands()
