from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userdata")
    address_1 = models.CharField(max_length=50, blank=False)
    address_2 = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=20, blank=False)
    town_or_city = models.CharField(max_length=50, blank=False)
    state_or_province = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.user.username + '_address'
    

