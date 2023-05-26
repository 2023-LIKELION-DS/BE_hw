from django.db import models

# Create your models here.
class Basic(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField(max_length=100)
  date = models.DateField(auto_now_add=True)
  
  def __str__(self):
    return self.title
  