import handbook as hb


def run():
    while True:
        hb.handbook_init()
        menu = get_menu()
        print_menu(menu)
        run_menu(menu)


def get_menu():
    return {
        '1': ['Посмотреть справочник', hb.view_all],
        '2': ['Добавить запись', hb.add_field],
        '3': ['Найти', hb.finde_in],
        '4': ['Удалить', hb.delete_line],
        '5': ['Импортировать', hb.import_file],
        '6': ['Экспортировать в txt', hb.save_txt],
        '7': ['Выход', exit]
    }


def print_menu(menu):
    for i, v in menu.items():
        print(f'{i} - {v[0]}')


def run_menu(menu):
    action = user_input(menu)
    menu[action][1]()


def user_input(menu):
    inp = ''
    while inp not in menu.keys():
        inp = input('Введите пункт меню ')
    return inp
