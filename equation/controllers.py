from decimal import Decimal
from math import sqrt
from django.core.exceptions import ObjectDoesNotExist
from equation.models import Parameter, Answer


def count_roots(a: float, b: float, c: float) -> tuple or str or float:
    """
    ПОдсчет корней уравнения
    """
    D = b ** 2 - 4 * a * c
    try:

        if D < 0:
            return
        elif D == 0:
            return round(-b / (2 * a), 2)
        else:
            root_1 = round((-b + sqrt(D)) / (2 * a), 2)
            root_2 = round((-b - sqrt(D)) / (2 * a), 2)
    except ZeroDivisionError:
        return round(-c / b, 2)

    return root_1, root_2


def get_roots(a: float = 1, b: float = 1, c: float = 1) -> list or str:
    try:
        answer = Answer.objects.get(
            parameter=Parameter.objects.get(a=a, b=b, c=c)
        )
        return [i for i in [answer.x_1, answer.x_2] if i]
    except ObjectDoesNotExist:
        roots = count_roots(a, b, c)
        parameter = Parameter.objects.create(
            a=a, b=b, c=c
        )
        if isinstance(roots, tuple):
            answer = Answer.objects.create(
                parameter=parameter,
                x_1=roots[0],
                x_2=roots[1]
            )
        elif isinstance(roots, int):
            answer = Answer.objects.create(
                parameter=parameter,
                x_1=roots,
            )
        else:
            answer = Answer.objects.create(
                parameter=parameter,
            )
        return [i for i in [answer.x_1, answer.x_2] if i]


if __name__ == '__main__':
    print(get_roots(1, 2, 3))
