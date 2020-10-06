import telebot
from connect_get_data_find import connect_and_get_data, find_number

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(func=lambda message: True, commands=['start', 'help'])
def handle_start_help(message):
    if message.text == '/help' or '/start':
        bot.send_message(message.chat.id, 'Привет! Я ищу номер телефона в базе контактов по ключу. '
                                          'Для старта напишите, например "/find"')


@bot.message_handler(func=lambda message: True, commands=['find'])
def handle_find(message):
        bot.send_message(message.chat.id, 'Окей, теперь напиши имя или фамилию, по которой будем искать.'
                                          'Будь внимателен, учитывай, что фамилия и имя должны начинаться с большой '
                                          'буквы, чтобы я корректно нашёл. Также ты можешь ввести часть '
                                          'имени или фамилии')
        bot.register_next_step_handler(message, found_result)


def found_result(message):
    key = message.text
    bot.send_message(message.chat.id, 'Начинаю поиск по ключу "{}"!'.format(message.text))
    answer = find_number(connect_and_get_data(), key)
    for i in range(0, len(answer)):
        bot.send_message(message.chat.id, answer[i])
    bot.send_message(message.chat.id, 'Если хочешь, мы можем попробовать снова. Просто напиши /find')


bot.polling(none_stop=True, interval=0)
