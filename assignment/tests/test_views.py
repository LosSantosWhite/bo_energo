from django.test import TestCase
from django.urls import reverse

from assignment.controllers import fill_db_with_items, get_item
from assignment.models import Item, Color


class AssignmentTest(TestCase):
    def setUp(self) -> None:
        color = "red"
        number = 4
        color = Color.objects.create(name=color)
        Item.objects.create(number=number, color=color)

    def test_view_response(self):
        response = self.client.get(reverse("assignment:get_item_view"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "assignment/index.html")

    def test_item_color(self):
        number = 4
        data = {"number": number}
        response = self.client.post(reverse("assignment:get_item_view"), data=data)

        self.assertContains(response, "Item color: red")

    def test_no_item(self):
        number = 400
        data = {"number": number}
        response = self.client.post(reverse("assignment:get_item_view"), data=data)

        self.assertContains(response, "Invalid number, must be lower than 100")
