from django.db import models

# Create your models here.

class Index(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

