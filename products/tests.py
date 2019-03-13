from django.test import TestCase
from .models import Product, ProductComment

class ProductTests(TestCase):
    print('Running Products Tests')
    """
    Create product in database
    Retrieve product from database
    Verify name, category
    Retrieve index and products and check for product
    """
    def test_add_product_to_database(self):
        product = Product(
            setnumber = '42',
            name = 'Zephod',
            category = 'Beeblebrox',
            price = 3.25,
            )
        product.save()
        product = Product.objects.filter(setnumber='42')
        self.assertEqual(str(product[0]), 
            '42 - Zephod - Beeblebrox')
        name = product[0].name
        self.assertIn('Zep',name)
        category = product[0].category
        self.assertEqual('Beeblebrox',category)
        index = self.client.get('/')
        self.assertEqual(index.status_code, 200)
        self.assertTemplateUsed(index, 'index.html')
        self.assertContains(index,'Zephod')
        products = self.client.get('/products/')
        self.assertEqual(products.status_code, 200)
        self.assertTemplateUsed(products, 'products.html')
        self.assertContains(products, 'Beeblebrox')

    """
    Render pages
    """
    def test_get_home_page(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')
    
    
    def test_get_products_page(self):
        page = self.client.get('/products/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'products.html')
    
    
    def test_get_product_detail_page(self):
        """
        Assert redirect for productdetail page
        """
        page = self.client.get('/products/1')
        self.assertEqual(page.status_code, 301)
