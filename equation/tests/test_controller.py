from django.test import TestCase
from equation.controllers import count_roots, get_roots
from equation.models import Answer, Parameter


class TestController(TestCase):
    @classmethod
    def setUpTestData(cls):
        parameter_1 = Parameter.objects.create(a=0, b=4, c=4)
        Answer.objects.create(parameter=parameter_1, x_1=-1)
        parameter_2 = Parameter.objects.create(a=10, b=2, c=10)
        Answer.objects.create(parameter=parameter_2)

    def test_count_1_root(self):
        self.assertEqual(count_roots(2, 4, 2), -1)

    def test_count_2_roots(self):
        self.assertEqual(count_roots(3.2, -7.8, 1), (2.3, 0.14))

    def test_zero_first_argument(self):
        self.assertEqual(count_roots(0, 4, 4), -1)

    def test_zero_second_arg(self):
        self.assertEqual(count_roots(1, 0, -1), (1, -1))

    def test_discriminant_lower_zero(self):
        self.assertEqual(count_roots(10, 2, 10), None)

    def test_get_value_from_db(self):
        self.assertEqual(get_roots(0, 4, 4), [-1])

    def test_get_value(self):
        self.assertEqual(get_roots(3.2, -7.8, 1), [2.3, 0.14])
        self.assertEqual(
            Answer.objects.get(parameter=Parameter.objects.get(a=3.2, b=-7.8, c=1)).x_1,
            2.3,
        )
        self.assertEqual(
            Answer.objects.get(parameter=Parameter.objects.get(a=3.2, b=-7.8, c=1)).x_2,
            0.14,
        )

    def test_no_roots(self):
        self.assertEqual(get_roots(10, 2, 10), [])
        self.assertEqual(
            Answer.objects.get(parameter=Parameter.objects.get(a=10, b=2, c=10)).x_2,
            None,
        )
