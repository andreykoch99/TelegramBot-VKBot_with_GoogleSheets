import gspread


def connect_and_get_data():
    res = gspread.service_account(filename='credentials.json').open_by_key(
        'TOKEN').sheet1.get_all_records()
    return res


def find_number(data):
    number_of_rows = len(data)
    answer = []
    print('Привет! По какому ключу (буквы фамилиии, имени) мы ищем?')
    find_me = input('!!! Будь внимателен, я чувствителен к регистру!!! (заглавные буквы, с которых начинаются имя и'
                    ' фамилия)\n')
    print('Начинаю поиск по ключу "{}"!'.format(find_me))
    for i in range(0, number_of_rows):
        if data[i]['имя'].find(find_me) != -1:
            answer.append(i)
            # print('Нашёл, это {}, её номер телефона: {}'.format(data[i]['имя'], data[i]['телефон']))
    if len(answer) == 1:
        print('Нашёл, это {}, её номер телефона: {}'.format(data[answer[0]]['имя'], data[answer[0]]['телефон']))
    elif len(answer) != 1 and len(answer) > 1:
        print('У меня есть {} вариантов, надеюсь, здесь есть то, что тебе нужно!'.format(len(answer)))
        for j in range(0, len(answer)):
            print('Вариант №{}, это {}, номер телефона: {}'.format(j + 1, data[answer[j]]['имя'], data[answer[j]]['телефон']))


find_number(connect_and_get_data())

# TODO Если ячейка 'телефон' пуста, то нужно это дополнительно предусмотреть при выводе
# TODO Добавить выбор листа в таблице и подумать, как подбирать столбцы для поиска
