from django.contrib import admin
from .models import Show
# Register your models here.

class myappAdmin(admin.ModelAdmin):
    list_display=['title','content','date','comment']
admin.site.register(Show,myappAdmin)  