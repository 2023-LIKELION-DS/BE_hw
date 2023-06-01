from django.db import models

# Create your models here.
class Show(models.Model):  #모델은 클레스로 선언, 뒤 모델 대문자 
    title=models.CharField(max_length=100)
    content=models.TextField(null=True)
    date=models.DateTimeField(auto_now=True)
    comment=models.CharField(max_length=50, null=True)  #다대다 관계 ..
    def __str__(self):
        return self.title