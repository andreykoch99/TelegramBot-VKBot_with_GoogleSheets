import telebot
from settings import TG_BOT_TOKEN, SEARCH_KEY, KEY_TO_FOUND
from connect_get_data_find import connect_and_get_data, find_number

bot = telebot.TeleBot(TG_BOT_TOKEN)


@bot.message_handler(func=lambda message: True, commands=['start', 'help'])
def handle_start_help(message):
    if message.text == '/help' or '/start':
        bot.send_message(message.chat.id, 'Привет! Я ищу номер телефона в базе контактов по ключу. '
                                          'Для старта напишите, например "/find"')


@bot.message_handler(func=lambda message: True, commands=['find'])
def handle_find(message):
    bot.send_message(message.chat.id,   'Окей, теперь напиши часть ключа "{}", по которому будет искаться "{}".'
                                        ' Будь внимателен, учитывай, что фамилия и имя должны начинаться с большой '
                                        'буквы, чтобы я корректно нашёл. Также ты можешь ввести часть '
                                        'имени или фамилии.'.format(SEARCH_KEY, KEY_TO_FOUND))
    bot.register_next_step_handler(message, found_result)
    # алгоритм следующий: 1) пользователь вводит команду /find, после скрипт отвечате и ожидает сообщение с ключом,
    # по которому будет осуществлён поиск. 2) вывод ответа происходит через цикл по списку, в котором лежат
    # ответы по ключу


def found_result(message):
    key = message.text
    bot.send_message(message.chat.id, 'Начинаю поиск по ключу "{}"!'.format(message.text))
    answer = find_number(connect_and_get_data(), key)
    for i in range(0, len(answer)):
        bot.send_message(message.chat.id, answer[i])
    bot.send_message(message.chat.id, 'Если хочешь, мы можем попробовать снова. Просто напиши /find')


bot.polling(none_stop=True, interval=0)
