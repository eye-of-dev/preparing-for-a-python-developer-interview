"""
1.  Проверить механизм наследования в Python. Для этого создать два класса.
    Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре:
    название и цену. Второй — дочерний (ItemDiscountReport), должен содержать
    функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке.
    Проверить работу программы, создав экземпляр (объект) родительского класса.
"""


class ItemDiscount:
    """
    Класс скидок
    """

    def __init__(self):
        self.title = 'Брюки'
        self.price = 2000


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
# ************* Module task01
# task01.py:10:0: R0903: Too few public methods (0/2) (too-few-public-methods)
# task01.py:18:0: R0903: Too few public methods (1/2) (too-few-public-methods)
#
# ------------------------------------------------------------------
# Your code has been rated at 7.14/10
