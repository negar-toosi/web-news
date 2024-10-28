from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Author)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'is_staff', 'is_active']
    search_fields = ('email',)  # Ensure you can search by email in the admin panel
    ordering = ('email',)  # Ensure the users are ordered by email

admin.site.register(CustomUser, CustomUserAdmin)
