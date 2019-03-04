from django.test import TestCase
from .models import Product, ProductComment

class ProductTests(TestCase):
    print('Running Products Tests')
    def test_str(self):
        product = Product(
            setnumber = '42',
            name = 'Zephod',
            category = 'Beeblebrox',
            price = 3.25,
            )
        product.save()
        product = Product.objects.filter(setnumber='42')
        self.assertEqual(str(product[0]), '42 - Zephod - Beeblebrox')
        name = product[0].name
        self.assertIn('Zep',name)
        category = product[0].category
        self.assertEqual('Beeblebrox',category)

    
    def test_get_home_page(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')
    
    def test_get_products_page(self):
        page = self.client.get('/products/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'products.html')
