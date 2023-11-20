import hashlib
import os
import pickle
import random
from collections import deque

import config

CACHE_FOLDER_PATH = "caches"

os.makedirs(CACHE_FOLDER_PATH, exist_ok=True)


def get_cache_path(cache_path):
    # Генерируем уникальный путь для кеша на основе хэша пути
    hash_object = hashlib.md5(cache_path.encode())
    hash_str = hash_object.hexdigest()
    return os.path.join(CACHE_FOLDER_PATH, f"cache_{hash_str}.pkl")


def load_cache(cache_path, max_cache_len):
    cache_path = get_cache_path(cache_path)
    try:
        with open(cache_path, "rb") as cache_file:
            return pickle.load(cache_file)
    except FileNotFoundError:
        return deque(maxlen=max_cache_len)
    except Exception as e:
        print(f"Ошибка при загрузке кеша для {cache_path}: {e}")
        return deque(maxlen=max_cache_len)


def save_cache(cache_path, cache):
    cache_path = get_cache_path(cache_path)
    try:
        with open(cache_path, "wb") as cache_file:
            pickle.dump(cache, cache_file)
    except Exception as e:
        print(f"Ошибка при сохранении кеша для {cache_path}: {e}")


def start_posting(data):
    # Выбираем аниме на основе весов
    choice = random.choices(data['anime_list'], weights=[item['chance'] for item in data['anime_list']], k=1)[0]
    # print(choice)

    # Получаем список файлов в выбранном каталоге аниме
    files = os.listdir(choice['path'])

    if choice['cache'].lower() == 'auto':
        total_files = len(files)
        max_cache_size = int(0.9 * total_files) if total_files > 100 else int(0.9 * total_files) - 11
    else:
        max_cache_size = choice['cache']

    # Получаем или создаем кеш для данного пути аниме
    cache = load_cache(choice['path'], max_cache_size)

    # Инициализируем пустой список для хранения выбранных файлов
    out = []

    while len(out) != 10:
        # Составляем путь к файлу
        file = choice['path'] + '/' + random.choice(files)

        # Проверяем, что файл не находится в кеше и является допустимым файлом
        if file not in out and file not in cache and os.path.isfile(file):
            out.append(file)

    while len(cache) > max_cache_size - 10:
        cache.popleft()

    # Добавляем файлы в кеш
    cache.extend(out)

    # Удаляем старые значения, если кеш превысил максимальный размер

    # Сохраняем кеш после каждого вызова start_posting
    save_cache(choice['path'], cache)

    return [choice['name'], out]
