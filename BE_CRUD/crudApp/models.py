from django.db import models

# Create your models here.
class Index(models.Model):
    title=models.CharField(max_length=100)  #방명록 제목   
    content=models.TextField(null=True)  #방명록 내용
    date=models.DateTimeField(auto_now=True, null=True)  #방명록 작성 시간 

    def __str__(self):  #방명록 제목으로 목록 확인 
        return self.title 