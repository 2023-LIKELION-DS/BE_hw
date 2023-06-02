from django.db import models

class Basic(models.Model):
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title