from django.test import TestCase


class TestEquationView(TestCase):
    def test_view_status(self):
        response = self.client.get("/equation/solve/")
        self.assertTemplateUsed(response, "equation/equation.html")
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        data = {"a": 1, "b": 2, "c": 3}
        response = self.client.post("/equation/solve/", data=data)
        self.assertContains(response, text="No real roots")
