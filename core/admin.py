from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import CustomUser, SocialPlatform, PartnerOrganization, ActivityPhoto, DonationCertificate
from django.contrib.admin.models import LogEntry
from django.contrib.admin.filters import DateFieldListFilter
from django.urls import reverse, NoReverseMatch
from django.utils.html import format_html
from django.utils.safestring import mark_safe
import json
from django.utils import timezone
from datetime import timedelta


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    ADDITION = 1
    CHANGE = 2
    DELETION = 3

    list_display = (
        'action_time',
        'user',
        'content_type',
        'object_repr',
        'colored_action_flag',
        'formatted_change_message',
        'object_link',
    )
    list_filter = (
        'user',
        'content_type',
        'action_flag',
        ('action_time', DateFieldListFilter),
    )
    search_fields = ('object_repr', 'change_message')
    readonly_fields = [f.name for f in LogEntry._meta.fields]
    ordering = ('-action_time',)
    date_hierarchy = 'action_time'
    list_per_page = 25

    def object_link(self, obj):
        if obj.action_flag == self.DELETION:
            return obj.object_repr
        try:
            ct = obj.content_type
            url = reverse(f'admin:{ct.app_label}_{ct.model}_change', args=[obj.object_id])
            return format_html('<a href="{}">{}</a>', url, obj.object_repr)
        except NoReverseMatch:
            return obj.object_repr
    object_link.short_description = 'Object Link'

    def colored_action_flag(self, obj):
        color_map = {
            self.ADDITION: 'green',
            self.CHANGE: 'orange',
            self.DELETION: 'red',
        }
        color = color_map.get(obj.action_flag, 'black')
        label = obj.get_action_flag_display()
        return format_html('<span style="color: {};">{}</span>', color, label)
    colored_action_flag.short_description = 'Action'

    def formatted_change_message(self, obj):
        try:
            message = json.loads(obj.change_message)
            if isinstance(message, list):
                parts = []
                for item in message:
                    if 'changed' in item:
                        fields = ', '.join(item['changed'].get('fields', []))
                        parts.append(f"Changed fields: <strong>{fields}</strong>")
                    if 'added' in item:
                        name = item['added'].get('name', 'object')
                        parts.append(f"Added <strong>{name}</strong>")
                    if 'deleted' in item:
                        name = item['deleted'].get('name', 'object')
                        parts.append(f"Deleted <strong>{name}</strong>")
                return mark_safe('<br>'.join(parts))
            return obj.change_message
        except (json.JSONDecodeError, TypeError):
            return obj.change_message
    formatted_change_message.short_description = 'Change Details'

    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    @admin.action(description="Delete LogEntries older than 6 months")
    def delete_old_logs_action(self, request, queryset):
        cutoff = timezone.now() - timedelta(days=180)
        old_logs = LogEntry.objects.filter(action_time__lt=cutoff)
        count = old_logs.count()
        old_logs.delete()
        self.message_user(request, f"Deleted {count} log entries older than 6 months.")
        
    @admin.action(description="Delete LogEntries older than 3 months")
    def delete_old_logs_action_2(self, request, queryset):
        cutoff = timezone.now() - timedelta(days=90)
        old_logs = LogEntry.objects.filter(action_time__lt=cutoff)
        count = old_logs.count()
        old_logs.delete()
        self.message_user(request, f"Deleted {count} log entries older than 3 months.")
    
    @admin.action(description="Delete LogEntries older than 1 month")
    def delete_old_logs_action_3(self, request, queryset):
        cutoff = timezone.now() - timedelta(days=30)
        old_logs = LogEntry.objects.filter(action_time__lt=cutoff)
        count = old_logs.count()
        old_logs.delete()
        self.message_user(request, f"Deleted {count} log entries older than 3 month.")
    
    @admin.action(description="Delete LogEntries older than 2 weeks")
    def delete_old_logs_action_4(self, request, queryset):
        cutoff = timezone.now() - timedelta(days=14)
        old_logs = LogEntry.objects.filter(action_time__lt=cutoff)
        count = old_logs.count()
        old_logs.delete()
        self.message_user(request, f"Deleted {count} log entries older than 2 weeks.")
    
    @admin.action(description="Delete LogEntries older than 1 week")
    def delete_old_logs_action_5(self, request, queryset):
        cutoff = timezone.now() - timedelta(days=7)
        old_logs = LogEntry.objects.filter(action_time__lt=cutoff)
        count = old_logs.count()
        old_logs.delete()
        self.message_user(request, f"Deleted {count} log entries older than 1 week.")
        
    actions = [delete_old_logs_action, delete_old_logs_action_2, delete_old_logs_action_3, delete_old_logs_action_4, delete_old_logs_action_5]


@admin.action(description="Make selected users as staff")
def make_as_staff(modeladmin, request, queryset):
    queryset.update(is_staff=True)

@admin.action(description="Make selected users as not staff")
def make_as_not_staff(modeladmin, request, queryset):
    queryset.update(is_staff=False)
    
@admin.action(description="Make selected users as active")
def make_as_active(modeladmin, request, queryset):
    queryset.update(is_active=True)

@admin.action(description="Make selected users as not active")
def make_as_not_active(modeladmin, request, queryset):
    queryset.update(is_active=False)


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
    
    ordering = ('date_joined',)
    actions = [make_as_staff, make_as_not_staff, make_as_active, make_as_not_active]

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


class SocialPlatformAdmin(admin.ModelAdmin):
    list_display = ('platform_name', 'url',)
    search_fields = ('platform_name', 'url',)
    readonly_fields = ()
    fieldsets = (
        (None, {
            'fields': ('platform_name', 'url',)
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.clean()
        super().save_model(request, obj, form, change)
    
    def has_module_permission(self, request):
        return request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_staff

    def has_add_permission(self, request):
        return request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff

admin.site.register(SocialPlatform, SocialPlatformAdmin)


class PartnerOrganizationAdmin(admin.ModelAdmin):
    list_display = ('org_name', 'website')
    search_fields = ('org_name', 'website')
        
    def has_module_permission(self, request):
        return request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_staff

    def has_add_permission(self, request):
        return request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff
    
admin.site.register(PartnerOrganization, PartnerOrganizationAdmin)


class ActivityPhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('caption',)
        
    def has_module_permission(self, request):
        return request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_staff

    def has_add_permission(self, request):
        return request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff
    
admin.site.register(ActivityPhoto, ActivityPhotoAdmin)

class DonationCertificateAdmin(admin.ModelAdmin):
    list_display = ('caption','certificate', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('caption','certificate',)

    def has_module_permission(self, request):
        return request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_staff

    def has_add_permission(self, request):
        return request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff

admin.site.register(DonationCertificate, DonationCertificateAdmin)