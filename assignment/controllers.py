import numpy as np
import random

from assignment.models import Item, Color


def fill_db_with_items():
    loc = 50
    output = np.random.normal(scale=50, loc=loc, size=100)
    red = [i for i in output if i < loc / 10]
    green = [i for i in output if i < loc and i not in red]
    blue = [i for i in output if i not in red and i not in green]

    num_list = random.sample(range(1, 101), 100)

    red_items_num = num_list[: len(red)]
    green_items_num = num_list[len(red) : len(red) + len(green)]
    blue_items_num = num_list[len(red) + len(green) :]

    for _, number in zip(red, red_items_num):
        Item.objects.create(color=Color.objects.get(name="red"), number=number)
    for _, number in zip(green, green_items_num):
        Item.objects.create(color=Color.objects.get(name="green"), number=number)
    for _, number in zip(blue, blue_items_num):
        Item.objects.create(color=Color.objects.get(name="blue"), number=number)


def refill_db():
    Item.objects.all().delete()
    fill_db_with_items()


def get_item(number: int) -> str:
    return Item.objects.get(number=number).color.name
