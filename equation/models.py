from django.db import models


class Parameter(models.Model):
    a = models.FloatField(verbose_name='Коэффициент a')
    b = models.FloatField(verbose_name='Коэффициент b')
    c = models.FloatField(verbose_name='Коэффициент c')

    def __str__(self):
        return f'Корни квадратного уравнения с коэффициентами ' \
               f'a={self.a}, b={self.b}, c={self.c}'


class Answer(models.Model):
    parameter = models.ForeignKey(Parameter, on_delete=models.PROTECT)
    x_1 = models.FloatField(null=True, verbose_name='Первый корень уравнения')
    x_2 = models.FloatField(null=True, verbose_name='Второй корень уравнения')
