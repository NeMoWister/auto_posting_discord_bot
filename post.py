import random
import os
import config
from collections import deque
import pickle
import hashlib


# Путь к основной папке, где будут храниться кеши
CACHE_FOLDER_PATH = "caches"

# Создаем каталог для хранения кешей, если его еще нет
os.makedirs(CACHE_FOLDER_PATH, exist_ok=True)


def get_cache_path(anime_path):
    # Генерируем уникальный путь для кеша на основе хэша пути к аниме
    hash_object = hashlib.md5(anime_path.encode())
    hash_str = hash_object.hexdigest()
    return os.path.join(CACHE_FOLDER_PATH, f"cache_{hash_str}.pkl")


def load_cache(anime_path, max_cache_len):
    cache_path = get_cache_path(anime_path)
    try:
        with open(cache_path, "rb") as cache_file:
            return pickle.load(cache_file)
    except FileNotFoundError:
        return deque(maxlen=max_cache_len)
    except Exception as e:
        print(f"Ошибка при загрузке кеша для {anime_path}: {e}")
        return deque(maxlen=max_cache_len)


def save_cache(anime_path, cache):
    cache_path = get_cache_path(anime_path)
    try:
        with open(cache_path, "wb") as cache_file:
            pickle.dump(cache, cache_file)
    except Exception as e:
        print(f"Ошибка при сохранении кеша для {anime_path}: {e}")


def start_posting():
    # Выбираем аниме на основе весов
    choice = random.choices(config.anime_list, weights=[item[2] for item in config.anime_list], k=1)[0]
    print(choice)

    # Получаем список файлов в выбранном каталоге аниме
    files = os.listdir(choice[1])

    # Получаем или создаем кеш для данного пути аниме
    cache = load_cache(choice[1], choice[3])

    # Инициализируем пустой список для хранения выбранных файлов
    out = []

    while len(out) != 10:
        # Составляем путь к файлу
        file = choice[1] + '/' + random.choice(files)

        # Проверяем, что файл не находится в кеше и является допустимым файлом
        if file not in out and file not in cache and os.path.isfile(file):
            out.append(file)

    while len(cache) > choice[3] - 10:
        cache.popleft()

    # Добавляем файлы в кеш
    cache.extend(out)

    # Удаляем старые значения, если кеш превысил максимальный размер

    # Сохраняем кеш после каждого вызова start_posting
    save_cache(choice[1], cache)

    print(out)
    return [choice[0], out]
