from django.test import TestCase
from assignment.controllers import fill_db_with_items, refill_db
from assignment.models import Item, Color


class TestController(TestCase):
    @classmethod
    def setUpTestData(cls):
        colors = ["red", "green", "blue"]
        for color in colors:
            Color.objects.create(name=color)

    def test_refill_db(self):
        fill_db_with_items()
        self.assertEqual(100, len(Item.objects.all()))
        self.assertTrue(
            len(Item.objects.filter(color__name="blue"))
            > len(Item.objects.filter(color__name="green"))
        )
        self.assertTrue(
            len(Item.objects.filter(color__name="green"))
            > len(Item.objects.filter(color__name="red"))
        )
        refill_db()
        self.assertEqual(100, len(Item.objects.all()))
        self.assertTrue(
            len(Item.objects.filter(color__name="blue"))
            > len(Item.objects.filter(color__name="green"))
        )
        self.assertTrue(
            len(Item.objects.filter(color__name="green"))
            > len(Item.objects.filter(color__name="red"))
        )
