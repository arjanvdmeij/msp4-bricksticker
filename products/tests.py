from django.test import TestCase
from .models import Product

class ProductTests(TestCase):
    def test_str(self):
        test_name = Product(
            setnumber = '3681',
            name = 'Amusement Park',
            category = 'Fabuland',
            )
        self.assertEqual(str(test_name), '3681 - Amusement Park - Fabuland')