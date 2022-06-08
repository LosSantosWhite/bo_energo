from unittest import TestCase
from equation.controller import get_roots


class TestController(TestCase):

    def test_get_1_root(self):
        self.assertEqual(
            get_roots(2, 4, 2), -1
        )

    def test_get_2_roots(self):
        self.assertEqual(
            get_roots(3.2, -7.8, 1), (2.3, 0.14)
        )

    def test_zero_first_argument(self):
        self.assertEqual(
            get_roots(0, 4, 4), -1
        )

    def test_zero_second_arg(self):
        self.assertEqual(
            get_roots(1, 0, -1), (1, -1)
        )

    def test_discriminant_lower_zero(self):
        self.assertEqual(
            get_roots(10, 2, 10), "Действительных корней нет"
        )
