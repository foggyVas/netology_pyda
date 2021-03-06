def to_order():
    person = int(input("Сколько будет гостей?: "))
    menu = print('Вот меню:', cook_book.keys())
    dishes = input('Напишите блюда из меню через пробел?: ').split(' ')
    shop_list = get_shop_list(dishes, person)
    print_order(shop_list)


def print_order(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'],
                                      shop_list_item['quantity'],
                                      shop_list_item['measure']))


def get_shop_list(dishes, person):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity']\
                    += new_shop_list_item['quantity']
    return shop_list


to_order()
