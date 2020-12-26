"""
3.  Создать два списка с различным количеством элементов.
    В первом должны быть записаны ключи, во втором — значения.
    Необходимо написать функцию, создающую из данных ключей и
    значений словарь. Если ключу не хватает значения,
    в словаре для него должно сохраняться значение None. Значения,
    которым не хватило ключей, необходимо отбросить.
"""

KEYS = [1, 'd', (5,), '45', 'word', 956]
VALUES = ['12', 54, 'abra_ka_da_bra', (5, 56, 78)]


def get_dict_from_lists(keys, values):
    """
    Создать словать из ключей и значений
    :param keys: Список ключей
    :param values: Список значений
    :return: Вернуть словарь
    """
    spam, len_values = {}, len(values)

    for index, val in enumerate(keys):
        if (index + 1) <= len_values:
            spam[val] = values[index]
        else:
            spam[val] = None

    return spam


MY_LIST = get_dict_from_lists(KEYS, VALUES)
print(MY_LIST)

# Результат
# {1: '12', 'd': 54, (5,): 'abra_ka_da_bra', '45': (5, 56, 78)}

# Результат pylint
# -------------------------------------------------------------------
# Your code has been rated at 10.00
