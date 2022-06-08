from decimal import Decimal
from math import sqrt


def get_roots(a: float = 1, b: float = 1, c: float = 1) -> tuple or str:
    """
    ПОдсчет корней уравнения
    """
    D = b ** 2 - 4 * a * c
    try:

        if D < 0:
            return "Действительных корней нет"
        elif D == 0:
            return round(-b / (2 * a), 2)
        else:

            root_1 = round((-b + sqrt(D)) / (2 * a), 2)
            root_2 = round((-b - sqrt(D)) / (2 * a), 2)
    except ZeroDivisionError:
        return round(-c / b, 2)

    return root_1, root_2


if __name__ == '__main__':
    print(get_roots(1, 0, -1))
