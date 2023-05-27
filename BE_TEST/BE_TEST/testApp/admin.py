from django.contrib import admin
from .models import Basic
# Register your models here.

class testAdmin(admin.ModelAdmin):
    list_display=['title','content', 'date']
admin.site.register(Basic, testAdmin)