from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=20, verbose_name="Color")

    def __str__(self):
        return self.name


class Item(models.Model):
    color = models.ForeignKey(
        Color, on_delete=models.PROTECT, verbose_name="Item color"
    )
    number = models.IntegerField(verbose_name="Item number", unique=True)

    def __str__(self):
        return f"{self.id} - {self.color.name}"
