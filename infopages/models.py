from django.db import models

class FAQ(models.Model):
    """
    Created to ensure easy updating of FAQ through admin
    panel instead of having to go through page HTML
    """
    question = models.CharField(max_length=254, default='')
    answer = models.TextField(default='')
    
    def __str__(self):
        return self.question
    
