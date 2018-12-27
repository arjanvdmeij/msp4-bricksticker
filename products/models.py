from django.db import models

class Product(models.Model):
    item_id = models.CharField(max_length=15, default='')
    name = models.CharField(max_length=254, default='')
    setnumber = models.DecimalField(max_digits=8,decimal_places=0)
    release_year = models.CharField(max_length=10, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image1 = models.ImageField(upload_to='img')
    image2 = models.ImageField(upload_to='img')
    category = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
    
