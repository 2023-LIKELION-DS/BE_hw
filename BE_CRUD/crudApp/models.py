from django.db import models

# Create your models here.
class Index(models.Model):
    title = models.CharField(max_length=100) #제목
    content = models.TextField(null=True) #내용 
    date = models.DateTimeField(auto_now_add=True) #작성 시간

def __str__(self):
    return self.title