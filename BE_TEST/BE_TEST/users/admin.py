from django.contrib import admin

from .models import User

@admin.register(User)
class AnswerModelAdmin(admin.ModelAdmin):
    pass