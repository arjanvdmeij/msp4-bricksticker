from django.test import TestCase
from .models import Product

class ProductTests(TestCase):
    def test_str(self):
        product = Product(
            setnumber = '42',
            name = 'Zephod',
            category = 'Beeblebrox',
            )
        self.assertEqual(str(product), '42 - Zephod - Beeblebrox')
    
    def test_get_home_page(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')
    
    def test_get_products_page(self):
        page = self.client.get('/products/')
        print(page)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'products.html')
