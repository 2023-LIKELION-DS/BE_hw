from django.contrib import admin
from .models import GuestBook

# Register your models here.
class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'datetime')

admin.site.register(GuestBook, GuestBookAdmin)