from django.db import models

# Create your models here.

class GuestBook(models.Model):
    title = models.CharField(max_length=50) ##방명록 제목
    author = models.CharField(max_length=10) ##방명록 작성자
    content = models.TextField(null=True) ##방명록 내용
    datetime = models.DateTimeField(auto_now_add=True) ##방명록 작성 시간

def __str__(self):
    return self.title