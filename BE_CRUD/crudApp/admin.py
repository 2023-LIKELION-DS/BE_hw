from django.contrib import admin
from .models import Index
# Register your models here.


class crudAppAdmin(admin.ModelAdmin):
    list_display=('title','content', 'date')
admin.site.register(Index, crudAppAdmin)
