from django.test import TestCase
from .models import Product

class ProductTests(TestCase):
    def test_str(self):
        test_name = Product(name='Thingy')
        self.assertEqual(str(test_name), 'Thingy')