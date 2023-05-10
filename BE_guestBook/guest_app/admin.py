from django.contrib import admin

# Register your models here.
from .models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'datetime')

admin.site.register(GuestBook, GuestBookAdmin)