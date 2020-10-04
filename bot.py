import telebot
from connect_get_data_find import connect_and_get_data, find_number

bot = telebot.TeleBot('TOKEN');

# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 'Привет! Я ищу номер телефона в базе конактов по ключу. '
                                      'По какому ключу начинаем поиск?')

@bot.message_handler(content_types=['text'])
def get_key(message):
    bot.send_message(message.chat.id, 'Начинаю поиск по ключу "{}"!'.format(message.text))
    key = message.text
    answer = find_number(connect_and_get_data(), key)
    for i in range(0, len(answer)):
        bot.send_message(message.chat.id, answer[i])



bot.polling(none_stop=True, interval=0)

