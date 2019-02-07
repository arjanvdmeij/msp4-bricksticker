from django.test import TestCase
from .models import Product

class ProductTests(TestCase):
    def test_str(self):
        print('Checking correct formatting of database item')
        test_name = Product(
            setnumber = '3681',
            name = 'Amusement Park',
            category = 'Fabuland',
            )
        self.assertEqual(str(test_name), '3681 - Amusement Park - Fabuland')
    
    def test_click_to_detail_product(self):
        print('Checking correct detail page is displayed')
        product = Product(id = 7)
        page = self.client.get('/products/{0}'.format(product.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'products/productdetail.html')