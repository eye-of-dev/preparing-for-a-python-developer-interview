"""
3.  Усовершенствовать родительский класс таким образом,
    чтобы получить доступ к защищенным переменным. Результат
    выполнения заданий 1 и 2 должен быть идентичным.
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
# Товар: Брюки - цена 2000

# Результат pylint
# ************* Module task03
# task03.py:39:4: W0235: Useless super delegation in method '__init__' (useless-super-delegation)
#
# ------------------------------------------------------------------
# Your code has been rated at 9.29/10
