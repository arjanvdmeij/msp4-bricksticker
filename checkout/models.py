from django.db import models
from products.models import Product

""" Main order containing customer information
"""
class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    address1 = models.CharField(max_length=40, blank=False)    
    address2 = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    state_or_province = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=40, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    email_address = models.EmailField(max_length=40, blank=False, default='')
    processed = models.BooleanField(default=False)
    date = models.DateField()
    
    def __str__(self):
        return "OrderID: {0} / Date: {1} / Processed: {2}".format(
            self.id, self.date, self.processed)

""" Order items to be grouped within the order
"""
class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)
    total_item_price = models.DecimalField(max_digits=6, decimal_places=2)
    
    @property
    def get_total_item_price(self):
        return self.product.price*self.quantity
    
    def __str__(self):
        self.total_item_price = self.get_total_item_price
        return "Qty: {0} / Item: {1} - {2} @ € {3} / Total: € {4}".format(
            self.quantity, self.product.setnumber, 
            self.product.name, self.product.price, 
            self.total_item_price
            )
