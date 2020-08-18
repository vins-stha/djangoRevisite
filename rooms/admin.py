from django.contrib import admin
from .models import Room,User

# Register your models here.
@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'email', 'password')
