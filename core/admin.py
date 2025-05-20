from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_superuser', 'is_active')
    ordering = ('email', 'username')
    search_fields = ('email', 'username')

    readonly_fields = ('last_login', 'date_joined')

    fieldsets = (
        ('User Information', {'fields': ('username', 'email', 'password')}),
        ('Authorizations', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Logs', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

admin.site.register(CustomUser, CustomUserAdmin)
