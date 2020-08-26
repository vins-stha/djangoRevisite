from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'date','desc']