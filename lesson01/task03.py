"""
Разработать генератор случайных чисел. В функцию передавать начальное и
конечное число генерации (нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.
"""
from random import shuffle


def my_random_func(start, end, count):
    """
    Генератор случайных чисел.
    :param start: начальное число генерации
    :param end: конечное число генерации
    :param count: колличество случайных чисел
    :return: Список случайних чисел
    """

    result_list, result_dict = [], {}
    spam = [val for val in range(start, end) if not val == 0]
    shuffle(spam)

    for key, val in enumerate(spam):
        if key == count:
            break

        result_list.append(val)
        result_dict[f'elem_{key}'] = val

    return result_list, result_dict


RESULT_LIST, RESULT_DICT = my_random_func(-10, 83, 5)

print(*RESULT_LIST)
print(*RESULT_DICT.values())
print(*RESULT_DICT.items())


# Результат
# 46 28 -2 81 73
# 46 28 -2 81 73
# ('elem_0', 46) ('elem_1', 28) ('elem_2', -2) ('elem_3', 81) ('elem_4', 73)

# Результат pylint
# --------------------------------------------------------------------
# Your code has been rated at 10.00/10
# WOW :)
