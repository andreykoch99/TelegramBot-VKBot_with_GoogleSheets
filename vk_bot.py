import vk_api
from settings import VK_BOT_TOKEN
from vk_api.longpoll import VkLongPoll, VkEventType
from connect_get_data_find import connect_and_get_data, find_number
from vk_api.utils import get_random_id

mytoken = VK_BOT_TOKEN
vk_session = vk_api.VkApi(token=mytoken)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def write_message(sender, text):
    vk_session.method('messages.send', {'user_id': sender, 'message': text, 'random_id': get_random_id()})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        msg = event.text
        sender = event.user_id
        ready_for_find = False

        if msg == 'Привет':
            write_message(sender, 'и тебе привет ')
        elif msg == '/start':
            write_message(sender, 'Привет! Я ищу номер телефона в базе контактов по ключу. '
                                  'Для старта напишите, например "/find"')

        elif msg == '/find':
            ready_for_find = True
            write_message(sender, 'Окей, теперь напиши имя или фамилию, по которой будем искать.'
                                  ' Будь внимателен, учитывай, что фамилия и имя должны начинаться с большой '
                                  'буквы, чтобы я корректно нашёл. Также ты можешь ввести часть '
                                  'имени или фамилии.')
        else:
            write_message(sender, 'Я тебя не понимаю')

        for event in longpoll.listen():
            if event.to_me and ready_for_find:
                key = event.text
                write_message(sender, 'Начинаю поиск по ключу "{}"!'.format(event.text))
                answer = find_number(connect_and_get_data(), key)
                for i in range(0, len(answer)):
                    write_message(sender, answer[i])
                write_message(sender, 'Если хочешь, мы можем попробовать снова. Просто напиши /find')
                ready_for_find = False
                break
