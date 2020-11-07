import gspread
from settings import GOOGLE_SHEET_TOKEN


def connect_and_get_data():
    res = gspread.service_account(filename='credentials.json').open_by_key(
        GOOGLE_SHEET_TOKEN).sheet1.get_all_records()
    return res


def find_number(data, key):
    number_of_rows = len(data)
    answer_db = []
    answer = []
    for i in range(0, number_of_rows):
        if data[i]['имя'].find(key) != -1:
            answer_db.append(i)
    if len(answer_db) == 1:
        answer.append(
            'Нашёл, это {}, номер телефона: {}'.format(data[answer_db[0]]['имя'], data[answer_db[0]]['телефон']))
    elif len(answer_db) != 1 and len(answer_db) > 1:
        answer.append('У меня есть {} вариантов, надеюсь, здесь есть то, что тебе нужно!'.format(len(answer_db)))
        for j in range(0, len(answer_db)):
            answer.append('Вариант №{}, это {}, номер телефона: {}'.format(j + 1, data[answer_db[j]]['имя'],
                                                                           data[answer_db[j]]['телефон']))
    elif len(answer_db) == 0:
        answer.append('По ключу "{}" ничего не найдено.'.format(key))
    return answer

# TODO Если ячейка 'телефон' пуста, то нужно это дополнительно предусмотреть при выводе
# TODO Добавить выбор листа в таблице и подумать, как подбирать столбцы для поиска
