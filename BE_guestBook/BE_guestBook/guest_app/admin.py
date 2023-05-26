from django.contrib import admin
from .models import GuestBook

class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'datetime')

admin.site.register(GuestBook, GuestBookAdmin)

# * admin / 1234 : admin 아이디 비밀번호 