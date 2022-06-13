from django.db import models


class Parameter(models.Model):
    a = models.FloatField(verbose_name="a")
    b = models.FloatField(verbose_name="b")
    c = models.FloatField(verbose_name="c")

    def __str__(self):
        return f"Equation roots " f"a={self.a}, b={self.b}, c={self.c}"


class Answer(models.Model):
    parameter = models.ForeignKey(Parameter, on_delete=models.PROTECT)
    x_1 = models.FloatField(null=True, verbose_name="1st root")
    x_2 = models.FloatField(null=True, verbose_name="2nd root")
