"""
4.  Написать программу, в которой реализовать две функции.
    В первой должен создаваться простой текстовый файл. Если
    файл с таким именем уже существует, выводим соответствующее
    сообщение. Необходимо открыть файл и подготовить два списка:
    с текстовой и числовой информацией. Для создания списков
    использовать генераторы. Применить к спискам функцию zip().
    Результат выполнения этой функции должен должен быть
    обработан и записан в файл таким образом, чтобы каждая строка
    файла содержала текстовое и числовое значение. Вызвать вторую
    функцию. В нее должна передаваться ссылка на созданный файл.
    Во второй функции необходимо реализовать открытие файла и простой
    построчный вывод содержимого. Вся программа должна запускаться по
    вызову первой функции.
"""
import os
import random


def get_string():
    """
    Генерация случайной строки
    :return: Случайная строка
    """
    return ''.join([chr(random.randint(97, 122)) for _ in range(11)])


def read_file(file_path):
    """
    Построчный вывод из файла в консоле
    :param file_path: Ссылка на файл
    :return: None
    """
    with open(file_path) as fn:
        for line in fn:
            print(line)


def prepare_file(text_list, numb_list):
    """
    Запись в файл комбинации строка - число
    :param text_list: Список случайних строк
    :param numb_list: Список случайных чисел
    :return: function
    """
    file_path = f'{os.path.abspath(os.getcwd())}/text.txt'

    if not os.path.exists(file_path):
        print('Файла не существует. Он будет создан')

    with open(file_path, 'w+') as fn:
        for text, numb in zip(text_list, numb_list):
            fn.write(f'{text} : {numb} \n')

    return read_file(file_path)


TEXT_LIST = [get_string() for _ in range(11)]
NUMB_LIST = [random.randint(10000, 99999) for _ in range(11)]

prepare_file(TEXT_LIST, NUMB_LIST)

# Результат
# euvarlarshd : 12475
# onhmedbpkui : 84253
# lugxvrsvmuo : 12719
# kkgcbokunga : 87649
# eudwyieiebz : 56143
# adptfqurccs : 24812
# valuhzxeftf : 33322
# wnvdrbywrva : 20193
# bvmlyzlokbf : 43327
# hnyafruslih : 64517
# fqafqrsxsvx : 26926

# Результат pylint
# ************* Module task04
# task04.py:34:28: C0103: Variable name "fn" doesn't conform to snake_case naming style (invalid-name)
# task04.py:51:34: C0103: Variable name "fn" doesn't conform to snake_case naming style (invalid-name)
#
# ------------------------------------------------------------------
# Your code has been rated at 8.95/10
