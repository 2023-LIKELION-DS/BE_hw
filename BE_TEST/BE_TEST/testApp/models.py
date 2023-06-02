from django.db import models

# Create your models here.

class Basic(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(null=True)
    date = models.DateField(auto_now_add=True)
    
    def __self__(self):
        return self.title