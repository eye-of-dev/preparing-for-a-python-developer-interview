"""
Дополнить следующую функцию недостающим кодом:

def print_directory_contents(sPath):
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
"""
import os


def print_directory_contents(path, result=[]):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    :param path: Папка для сканирования
    :param result: результут
    :return: Список всех вложенных файлов
    """
    base_path = f'{os.path.abspath(os.getcwd())}/{path}'
    for x_file in sorted(os.listdir(base_path)):
        result.append(f'{path}/{x_file}')
        if os.path.isdir(f'{base_path}/{x_file}'):
            print_directory_contents(f'{path}/{x_file}', result)

    return result


LISTING = print_directory_contents('dir_test')

for val in LISTING:
    print(val)

# Результат
# dir_test/sub_dir
# dir_test/sub_dir/.geek
# dir_test/sub_dir_two
# dir_test/sub_dir_two/any_file.py
# dir_test/test.py

# Результат pylint
# ************* Module task02
# task02.py:16:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
#
# ------------------------------------------------------------------
# Your code has been rated at 9.09/10

# Не понял, чем опасны инициализация пустого списка в аргумерте функции
