from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    setnumber = models.DecimalField(max_digits=8,decimal_places=0)
    release_year = models.CharField(max_length=10, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image1 = models.ImageField(upload_to='img')
    image2 = models.ImageField(upload_to='img')
    category = models.CharField(max_length=100, default='')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.setnumber, 
                                        self.name, 
                                        self.category)

class ProductComment(models.Model):
    comment_on = models.ForeignKey(
        Product, on_delete=models.CASCADE, 
        related_name="Product_Comment")
    author = models.CharField(max_length=75)
    content = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}".format(self.date)