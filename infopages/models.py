from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=254, default='')
    answer = models.TextField(default='')
    
    def __str__(self):
        return self.question
    
