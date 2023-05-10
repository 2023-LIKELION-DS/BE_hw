from django.db import models

# Create your models here.
class GuestBook(models.Model):
    title = models.CharField(max_length=50)    #방명록 제목
    author = models.CharField(max_length=10)   
    content = models.TextField(null=True)
    datetime = models.DateTimeField(auto_now_add=True)      #settings.py에서 time_zone을 대한민국 시간으로 설정된 작성시간으로 바꿔줌
    
    def __str__(self):
        return self.title       #방명록 제목(title)으로 목록 확인