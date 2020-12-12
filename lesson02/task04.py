"""
4.  Реализовать возможность переустановки значения цены товара.
    Необходимо, чтобы и родительский, и дочерний классы получили
    новое значение цены. Следует проверить это, вызвав соответствующий
    метод родительского класса и функцию дочернего (функция, отвечающая
    за отображение информации о товаре в одной строке).
"""


class ItemDiscount:
    """
    Класс скидок
    """

    def __init__(self):
        self.__title = 'Брюки'
        self.__price = 2000

    @property
    def title(self):
        """

        :return:
        """
        return self.__title

    @property
    def price(self):
        """

        :return:
        """
        return self.__price

    @title.setter
    def title(self, value):
        """

        :param value:
        :return:
        """
        self.__title = value

    @price.setter
    def price(self, value):
        """

        :param value:
        :return:
        """
        self.__price = value


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


item = ItemDiscountReport()
item.title = 'Рубашка'
item.price = 4000

print(item.get_parent_data())

# Результат
# Товар: Рубашка - цена 4000

# Результат pylint
# ************* Module task04
# task04.py:59:4: W0235: Useless super delegation in method '__init__' (useless-super-delegation)
# task04.py:70:0: C0103: Constant name "item" doesn't conform to UPPER_CASE naming style (invalid-name)
#
# ------------------------------------------------------------------
# Your code has been rated at 9.05
