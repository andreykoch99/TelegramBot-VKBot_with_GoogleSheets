# Telegram и VKBot, работающие с GoogleSheets

## Установка
* Создать виртуальное окружение
* Установить пакеты из `requirements.txt`
* Для GoogleSheets необходимо создать credentials.json и настроить доступ к
вашей таблице, рекомендую: https://www.youtube.com/watch?v=Bnoth-4Z8m8
* Для TelegramBot'а необходимо получить token у BotFather, 
подробнее: https://www.youtube.com/watch?v=jPRYwY_O-3A
* Для VKBot'а необходимо создать группу и получить token,
подробнее: https://www.youtube.com/watch?v=eeNwyN8w8F0


##Функционал
* Алгоритм позволяет запустить одного из двух(или оба бота), 
чтобы принимать из Telegram или VK ключи, по которым будет осуществляться поиск
в подключенной Google Таблице по ключу SEARCH_KEY c выводом по нему KEY_TO_FOUND
