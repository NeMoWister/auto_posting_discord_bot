import random
import os
import config
from collections import deque
import pickle
import hashlib


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


def start_posting():
    # Выбираем путь на основе весов
    choice = random.choices(config.my_list, weights=[item[2] for item in config.my_list], k=1)[0]
    print(choice)

    # Получаем список файлов в выбранном каталоге
    files = os.listdir(choice[1])

    if choice[3].lower() == 'auto':
        total_files = len(files)
        max_cache_size = int(0.9 * total_files) if total_files > 100 else int(0.9 * total_files) - 10
    else:
        max_cache_size = choice[3]
        
    # Получаем или создаем кеш для данного пути
    cache = load_cache(choice[1], choice[3])

    # Инициализируем пустой список для хранения выбранных файлов
    out = []

    while len(out) != 10:
        # Составляем путь к файлу
        file = choice[1] + '/' + random.choice(files)

        # Проверяем, что файл не находится в кеше и является допустимым файлом
        if file not in out and file not in cache and os.path.isfile(file):
            out.append(file)

    while len(cache) > max_cache_size - 10:
        cache.popleft()

    # Добавляем файлы в кеш
    cache.extend(out)

    # Удаляем старые значения, если кеш превысил максимальный размер

    # Сохраняем кеш после каждого вызова start_posting
    save_cache(choice[1], cache)

    print(out)
    return [choice[0], out]
