from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User=get_user_model()  #코드를 변경하지 않고 바로 쓴느방법

class Post(models.Model):  #1관계 
    image=models.ImageField(verbose_name='이미지', null=True, blank=True)
    content=models.TextField(verbose_name='내용')
    created_at=models.DateTimeField(verbose_name='작성일', auto_now_add=True)  #셍성되면 자동으로 넣어주는 속
    view_count=models.IntegerField(verbose_name='조회수', default=0)  
    writer=models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)  #공백 허용 to속성과 on_delete필수

class Comment(models.Model):  #다 관계. 1을 참조해야함
    content=models.TextField(verbose_name='내용')
    created_at=models.DateTimeField(verbose_name='작성일',auto_now_add=True)
    post=models.ForeignKey(to='Post', on_delete=models.CASCADE) #위가 삭제되면 게시글 다 삭제된다.
    writer=models.ForeignKey(to=User, on_delete=models.CASCADE,null=True, blank=True)