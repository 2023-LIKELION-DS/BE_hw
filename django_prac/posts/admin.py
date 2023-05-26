from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'content', 'created_at', 'view_count', 'writer')
    # list_filter = ('created_at', )
    
    
admin.site.register(Comment)

