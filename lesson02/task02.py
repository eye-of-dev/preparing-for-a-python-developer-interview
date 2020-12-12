"""
2.  Инкапсулировать оба параметра (название и цену) товара родительского класса.
    Убедиться, что при сохранении текущей логики работы программы
    будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    """
    Класс скидок
    """

    def __init__(self):
        self.__title = 'Брюки'
        self.__price = 2000


class ItemDiscountReport(ItemDiscount):
    """
    Отчет по скидкам на товар
    """

    def __init__(self):
        super(ItemDiscountReport, self).__init__()

    def get_parent_data(self):
        """
        Возвращает данные из родительского класс
        :return: Строка
        """
        return f'Товар: {self.title} - цена {self.price}'


print(ItemDiscountReport().get_parent_data())

# Результат
# Traceback (most recent call last):
#   File "/lesson02/task02.py", line 29, in <module>
#     print(ItemDiscountReport().get_parent_data())
#   File "/lesson02/task02.py", line 26, in get_parent_data
#     return f'Товар: {self.title} - цена {self.price}'
# AttributeError: 'ItemDiscountReport' object has no attribute '_ItemDiscountReport__title'
