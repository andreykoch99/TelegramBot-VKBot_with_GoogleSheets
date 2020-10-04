import gspread


def connect_and_get_data():
    res = gspread.service_account(filename='credentials.json').open_by_key(
        'TOKEN').sheet1.get_all_records()
    return res


def find_number(data, key):
    number_of_rows = len(data)
    answer_db = []
    answer = []
    # print('Привет! По какому ключу (буквы фамилиии, имени) мы ищем?')
    # find_me = input('!!! Будь внимателен, я чувствителен к регистру!!! (заглавные буквы, с которых начинаются имя и'
    #                 ' фамилия)\n')
    # print('Начинаю поиск по ключу "{}"!'.format(find_me))
    for i in range(0, number_of_rows):
        if data[i]['имя'].find(key) != -1:
            answer_db.append(i)
    if len(answer_db) == 1:
        answer.append('Нашёл, это {}, номер телефона: {}'.format(data[answer_db[0]]['имя'], data[answer_db[0]]['телефон']))
    elif len(answer_db) != 1 and len(answer_db) > 1:
        answer.append('У меня есть {} вариантов, надеюсь, здесь есть то, что тебе нужно!'.format(len(answer_db)))
        for j in range(0, len(answer_db)):
            answer.append('Вариант №{}, это {}, номер телефона: {}'.format(j + 1, data[answer_db[j]]['имя'],
                                                                   data[answer_db[j]]['телефон']))
    return answer

# print(find_number(connect_and_get_data(), 'Ма'))

# TODO Если ячейка 'телефон' пуста, то нужно это дополнительно предусмотреть при выводе
# TODO Добавить выбор листа в таблице и подумать, как подбирать столбцы для поиска
