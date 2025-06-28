from django.contrib import admin
from .models import ContactMessage

@admin.action(description="Mark selected messages as replied")
def mark_as_replied(modeladmin, request, queryset):
    queryset.update(is_replied=True)

@admin.action(description="Mark selected messages as not replied")
def mark_as_not_replied(modeladmin, request, queryset):
    queryset.update(is_replied=False)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'email', 'ph_number', 'subject', 'message', 'sent_at', 'is_replied')
    list_filter = ('sent_at', 'is_replied')
    search_fields = ('sender', 'email', 'subject', 'message')
    readonly_fields = ('sender', 'email', 'ph_number', 'subject', 'message', 'sent_at')

    fieldsets = (
        ('Sender Informations', {
            'fields': ('sender', 'email', 'ph_number')
        }),
        ('Message Informations', {
            'fields': ('subject', 'message', 'sent_at', 'is_replied')
        }),
    )

    ordering = ('-sent_at',)
    actions = [mark_as_replied, mark_as_not_replied]

    def has_module_permission(self, request):
        return request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_staff

    def has_add_permission(self, request):
        return False  

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        return self.readonly_fields + ('is_replied',)

admin.site.register(ContactMessage, ContactMessageAdmin)
