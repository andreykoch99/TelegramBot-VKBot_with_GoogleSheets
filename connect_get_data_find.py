import gspread
from settings import GOOGLE_SHEET_TOKEN, SEARCH_KEY, KEY_TO_FOUND


def connect_and_get_data():
    res = gspread.service_account(filename='credentials.json').open_by_key(
        GOOGLE_SHEET_TOKEN).sheet1.get_all_records()
    return res


def find_number(data, key_from_user):
    number_of_rows = len(data)  # data - все данные из таблицы, len показывает количество строк в таблице
    # data - это словарь, в котором находится n кол-во строк, а в каждой строке лежат
    # ключи (это заголовки столбцов), в их значениях лежат содержимое ячейки
    answer_db = []  # список со скопированными строками из data, в которых есть соответствия по ключам
    answer = []     # список со строками, в которых сформирован ответ для пользователя, где даётся значение
    #   SEARCH_KEY и KEY_TO_FOUND
    for i in range(0, number_of_rows):
        if data[i][SEARCH_KEY].find(key_from_user) != -1:  # Поиск в таблице (data) по [строке] и [заданному из настроек
            answer_db.append(i)  # ключу] по ключу от пользователя (key_from_user)
    if len(answer_db) == 1: # Найдено одно соответствие
        answer.append(
            'Нашёл, это {}, {}: {}'.format(data[answer_db[0]][SEARCH_KEY], KEY_TO_FOUND,
                                           data[answer_db[0]][KEY_TO_FOUND]))
    elif len(answer_db) != 1 and len(answer_db) > 1:    # Найден несколько соответствий
        answer.append('У меня есть {} вариантов, надеюсь, здесь есть то, что тебе нужно!'.format(len(answer_db)))
        for j in range(0, len(answer_db)):
            answer.append('Вариант №{}, это {}, {}: {}'.format(j + 1, data[answer_db[j]][SEARCH_KEY],
                                                               KEY_TO_FOUND,
                                                               data[answer_db[j]][KEY_TO_FOUND]))
    elif len(answer_db) == 0:   # Соответствий не найдено
        answer.append('По ключу "{}" ничего не найдено.'.format(key_from_user))
    return answer

# TODO Если ячейка 'телефон' пуста, то нужно это дополнительно предусмотреть при выводе
# TODO Добавить выбор листа в таблице и подумать, как подбирать столбцы для поиска
