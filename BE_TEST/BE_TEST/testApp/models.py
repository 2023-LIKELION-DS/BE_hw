from django.db import models

# Create your models here.
class Basic(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField
    # content = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now=True)
    
    
# def __str__(self):
#     return self.titles