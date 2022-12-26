import os as os
import re as re


path = 'handbook.csv'
handler = ['id', 'Фамилия:', 'Имя:', 'Телефон:', 'Описание:']


def view_all():
    global path
    print_table(open_file(path))


def open_file(path):
    match path[-3:]:
        case 'csv':
            return open_csv(path)
        case 'txt':
            return open_txt(path)
        case _:
            return print('Расширение не поддерживается ')


def open_csv(path):
    field = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            field.append(line.strip().split(','))
    return field


def open_txt(path):
    field = []
    l = []
    i = 0
    with open(path, 'r', encoding='utf-8') as file:
        for lines in file:
            l.append(lines.strip())
            i += 1
            if i == 5:
                i = 0
                field.append(l)
                l = []
    return field


def print_table(field):
    global handler
    # Получение максимальной длинны каждого столбца
    maxlen = []
    field.insert(0, handler)
    for i in range(len(field[0])):
        maxlen.append(max([len(k[i]) for k in field]))

    # Вывод таблицей
    for line in field:
        print(f'{line[0].ljust(maxlen[0])}\t{line[1].ljust(maxlen[1])}\t{line[2].ljust(maxlen[2])}\t{line[3].ljust(maxlen[3])}\t{line[4].ljust(maxlen[4])}\t')


def add_field():
    global path
    inp = input_line()

    with open(path, 'r', encoding='utf-8') as file:
        try:
            index = int(file.readlines()[-1].split(',')[0])+1
        except:
            index = 1

    with open(path, 'a+', encoding='utf-8') as file:
        file.writelines(f'{index},{",".join(inp)}\n')
    print('Новая запись добавлена.')


def input_line():
    return [text_validate("Введите фамилию"),
            text_validate('Введите имя'),
            phone_validate(),
            input('Введите описание\n')]


def phone_validate():
    phone = input("Введите телефон\n")
    if re.fullmatch(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', phone):
        return phone
    else:
        print('Телефон не распознан')
        return phone_validate()


def text_validate(name):
    text = input(f"Введите {name}\n")
    if re.fullmatch(r'^[A-Za-zА-Яа-я]{3,}$', text.lower()):
        return text.title()
    else:
        print('Вы ввели недопустимые символы')
        return text_validate(name)


def finde_validate():
    text = input(f"Введите поисковой запрос\n")
    if re.fullmatch(r'^[0-9A-Za-zА-Яа-я]+$', text.lower()):
        return text.title()
    else:
        print('Вы ввели недопустимые символы, либо слишком короткий поисковой запрос')
        return finde_validate()


def index_validate():
    text = input(f"Введите индекс строки джля удаления\n")
    if re.fullmatch(r'^[0-9]+$', text.lower()):
        return text.title()
    else:
        print('Вы ввели недопустимые символы ')
        return index_validate()


# Создаем рабочий файл если его нет
def handbook_init():
    global path
    if not os.path.exists(path):
        with open(path, 'w') as file:
            print(f'Создан рабочий файл справочника\n')


def finde_in():
    global path
    file = open_file(path)

    search = finde_validate().lower()
    finded = []

    for i in range(1, len(file)):
        for f in file[i]:
            if search in f.lower():
                # print(re.search(search, f))
                finded.append(file[i])
                continue

    print_table(finded)


def delete_line():
    global path

    index = int(index_validate())-1
    file = open_file(path)

    if index > len(file):
        return print('Такой записи не существует')
    file.pop(index)
    for i in range(index, len(file)+1):
        file[i-1][0] = f'{i}'

    save_csv(file)

    print('Запись удалена, индексы обновлены')


def save_txt():
    global path

    file = open_file(path)

    with open(path[:-3]+'txt', 'w', encoding='utf-8') as f:
        for lines in file:
            for i in lines:
                f.writelines(f"{i}\n")


def input_file_name():
    file_name = input(f"Введите имя файла\n")
    if re.fullmatch(r'^[0-9A-Za-zА-Яа-я]+[.]{1}[0-9A-Za-z]{2,}$', file_name.lower()):
        return file_name
    else:
        print('Вы ввели недопустимое имя файла')
        return input_file_name()


def save_csv(file):
    with open(path, 'w', encoding='utf-8') as f:
        for lines in file:
            f.writelines(f"{','.join(lines)}\n")


def import_file():
    global path

    file_name = input_file_name()
    # file_name = 'handbook.txt'
    new_file = open_file(file_name)

    if new_file:
        old_file = open_file(path)
        try:
            index = int(old_file[-1][0])
        except:
            index = 1
        old_file.extend(new_file)

        for i in range(index, len(old_file)):
            old_file[i][0] = str(i + 1)

        save_csv(old_file)

        print_table(old_file)
        print('Файл импортирован')
    else:
        print('Файл не распознан')
