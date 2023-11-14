# Discord Auto Posting Bot

Этот Discord-бот выбирает случайные изображения из предварительно определенных папок и отправляет их в заданный канал.

## Как использовать

1. Установите все необходимые зависимости, выполнив:

    ```
    pip install -r requirements.txt
    ```

2. Укажите настройки бота в файле `config.py` такие как:

    ```python
    # config.py
    token = 'your discord token'
    my_list = [('name', 'path', chance, max_cache_size)]
    channel_id = int # id вашего дискорд канала
    ```
    Рекомендую max_cache_size ставить близко к общему количеству файлов в папке 
    
3. Запустите бота с помощью:

    ```
    python bot.py
    ```

Бот будет случайным образом выбирать 10 изображений из указанных папок и отправлять их в заданный канал.

## Настройки кеширования

Бот автоматически кеширует отправленные изображения, чтобы избежать повторной отправки в том же сеансе. Кеш хранится для каждой папки отдельно.

## Конфигурация

В файле `config.py` вы можете настроить список папок, их пути, веса для случайного выбора и максимальное значение кеша.

## Лицензия
Этот проект распространяется под лицензией [CC0 (Creative Commons Zero)](LICENSE).
