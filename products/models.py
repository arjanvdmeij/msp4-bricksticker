from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    setnumber = models.DecimalField(max_digits=8,decimal_places=0)
    short_description = models.CharField(max_length=254, default='')
    long_description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image1 = models.ImageField(upload_to='img')
    image2 = models.ImageField(upload_to='img')
    main_category = models.CharField(max_length=100, default='')
    sub_category = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.name
    
