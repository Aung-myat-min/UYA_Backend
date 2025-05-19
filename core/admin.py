from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'date_joined', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

admin.site.register(CustomUser, CustomUserAdmin)
