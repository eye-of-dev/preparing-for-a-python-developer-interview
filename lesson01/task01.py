"""
Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
Первый и второй множитель должны задаваться в виде аргументов функции.
Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
Полученная строка выводится в главной функции.
Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.
"""
from tabulate import tabulate

ARG_ONE = int(input('Введите 1-ый множитель: '))
ARG_TWO = int(input('Введите 2-ый множитель: '))


def mod_table(arg_x, arg_y):
    """
    Вывод таблицы Пифагора
    :param arg_x: Первый множитель
    :param arg_y: Второй множитель
    :return: None
    """

    result = []

    x_line = [x for x in range(arg_x + 1)]
    y_line = [x for x in range(arg_y + 1) if x > 0]

    for x_val in x_line:
        spam = [x_val]

        for y_val in y_line:
            spam.append(y_val * x_val if x_val > 0 else y_val)

        result.append(spam)

    print(tabulate(result))


mod_table(ARG_ONE, ARG_TWO)

# Результат программы
# -  -  --  --  --  --
# 0  1   2   3   4   5
# 1  1   2   3   4   5
# 2  2   4   6   8  10
# 3  3   6   9  12  15
# 4  4   8  12  16  20
# 5  5  10  15  20  25
# -  -  --  --  --  --

# Результат pylint
# ************* Module task01
# task01.py:9:0: E0401: Unable to import 'tabulate' (import-error)
# task01.py:25:0: R1721: Unnecessary use of a comprehension (unnecessary-comprehension)
#
# ------------------------------------------------------------------
# Your code has been rated at 5.71/10
#
# P.S. не понял как решить:(
