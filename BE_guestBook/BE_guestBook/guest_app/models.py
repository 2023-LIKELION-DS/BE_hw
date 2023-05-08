from django.db import models

# Create your models here.

class GuestBook(models.Model):
  title = models.CharField(max_length=50)
  author = models.CharField(max_length=10)
  content = models.TextField()
  datetime = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
      return self.title
  