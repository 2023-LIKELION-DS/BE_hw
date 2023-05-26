from django.contrib import admin
from .models import Index

class IndexAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date')

# Register your models here.
admin.site.register(Index, IndexAdmin)